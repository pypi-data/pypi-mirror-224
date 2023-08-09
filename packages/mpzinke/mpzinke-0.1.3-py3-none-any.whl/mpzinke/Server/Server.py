#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2023.07.31                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from flask import Flask, jsonify
from flask_cors import CORS
import sys
import traceback
from typing import Dict, Optional, TypeVar
from werkzeug.exceptions import Forbidden, HTTPException, Unauthorized


from .Route import Route, HTTP_METHOD, URL


class Server:
	"""
	Flask API Server.
	Methods:
		- __init__:
	"""
	EXCEPTIONS = {401: Unauthorized, 403: Forbidden}


	def __init__(self, *, authorization: Optional[callable]=None, handle_error: Optional[callable]=None,
	  host: str="0.0.0.0", name: str="Flask App", port: int=8080, version: str="1.0.0", **kwargs: dict
	):
		self._app = Flask(name, **kwargs)

		self._cors = CORS(self._app)
		self._app.config['CORS_HEADERS'] = 'Content-Type'
		self._app.register_error_handler(Exception, self._handle_error)
		self._app.after_request(self._after_request)

		self._authorization: callable = authorization
		self._handle_error = handle_error or self._handle_error
		self._host: str = host
		self._port: int = port
		self._routes: list[Route] = []
		self._version: str = version

		self.jinja_env = self._app.jinja_env


	# ———————————————————————————————————————————————————— THREAD ———————————————————————————————————————————————————— #

	def __call__(self) -> None:
		"""
		SUMMARY: Adds routes to server & class, and starts the server instance.
		DETAILS: Sets routes using hardcoded routes, functions & HTTP request methods. Calls the Flask::run method.
		"""
		self._app.run(host=self._host, port=self._port)


	# ——————————————————————————————————————————————— REQUEST HANDLING ——————————————————————————————————————————————— #

	def _after_request(self, response):
		"""
		FROM: https://stackoverflow.com/a/30717205
		"""
		response.headers["Version"] = self._version
		return response


	def debug(self, flag: bool=True) -> None:
		self._app.debug = flag


	def _handle_error(self, error):
		"""
		SUMMARY: Handles the return response for any server error that occurs during a request.
		PARAMS:  Takes the error that has occured.
		RETURNS: The JSON of the error.
		FROM: https://readthedocs.org/projects/pallet/downloads/pdf/latest/
		 AND: https://stackoverflow.com/a/29332131
		"""
		if isinstance(error, HTTPException):
			return jsonify(error=str(error)), error.code

		try:
			exception_traceback = traceback.format_exc()
		except:
			exception_traceback = "Unknown traceback"

		print(str(error), exception_traceback, file=sys.stderr)
		return jsonify(error=str(error), traceback=exception_traceback), 500


	# ————————————————————————————————————————————————————— AUTH ————————————————————————————————————————————————————— #

	@staticmethod
	def bearer_auth(*authorization_args: list) -> callable:
		use_message = "Use either statically with `Server.bearer_auth(auth: str)`" \
		  + " or dynamically with `<server_object>.bearer_auth(auth: str)`"
		if(len(authorization_args) == 0):
			raise TypeError(f"An authorization string must be passed to `bearer_auth`\n{use_message}")

		if(len(authorization_args) > 2):
			raise TypeError(f"Too many arguments passed\n{use_message}")

		if(len(authorization_args) == 1):
			if(not isinstance(authorization_args[0], str)):
				raise TypeError(f"Invalid argument passed\n{use_message}")

			authorization = authorization_args[0]

		elif(len(authorization_args) == 2):
			if(not isinstance(authorization_args[0], Server) or not isinstance(authorization_args[1], str)):
				raise TypeError(f"Invalid argument passed\n{use_message}")

			authorization = authorization_args[1]

		def check_auth(request) -> bool:
			if("Authorization" not in request.headers):
				raise Unauthorized()

			elif(request.headers["Authorization"] != f"Bearer {authorization}"):
				raise Forbidden()

		return check_auth


	@staticmethod
	def no_auth(*_: list) -> True:
		return True


	# ———————————————————————————————————————————————————— ROUTES ———————————————————————————————————————————————————— #
	# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————— #

	def route(self, url: URL, GET: callable=None, *, additional_args: Dict[type, any]=None,
	  authorization: Optional[callable]=None, **method_mappings: Dict[HTTP_METHOD, callable]
	) -> None:
		"""
		SUMMARY: 
		PARAMS:  
		DETAILS: 
		"""
		additional_args = additional_args or {}
		method_mappings = {method.upper(): function for method, function in method_mappings.items()}

		if(GET is not None):  # Use the GET argument
			if("GET" in [key.upper() for key in method_mappings]):  # Ensure 'GET' is not doubly supplied
				raise Exception(f"Ambiguous supplying of argument 'GET' and keyword argument 'GET' for URL '{url}'")

			method_mappings["GET"] = GET

		authorization = authorization or self._authorization
		route = Route(self, url, method_mappings, additional_args=additional_args, authorization=authorization)
		self._routes.append(route)

		# Set URLs for both urls that do and do not end with '/', with the exception of the root URL
		# Get the url without and with the ending '/', then remove the blank urls (ie if the root url is provided)
		urls = set(url for url in [url.rstrip("/"), (f"{url}/" if(url[-1] != "/") else url)] if(url))
		[self._app.add_url_rule(url, url, route, methods=list(method_mappings)) for url in urls]
