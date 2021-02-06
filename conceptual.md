### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript? 
  * Python is meant to handle all server-side functions, page changes, requests, redirections, etc. While JS is made for client-side things like manipulating the dom or changing things on the currently viwed page.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  * Use get() and specify a default value  if not present
  * Use setdefault() to create a new key if not present
  * Use a _try except_ block to handle if there is an error so it doesn't crash program

- What is a unit test?
  * Tests individual components for proper function

- What is an integration test?
  * Tests how components function together to achieve desired results

- What is the role of web application framework, like Flask?
  * Provides a set of functions, classes and other helpers to standardize and make creating a web application easier.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  * Typically a url param specifies which page to go to (subject of page) and a query param acts more like a modifier to show specific information on the page.

- How do you collect data from a URL placeholder parameter using Flask?
  * @app.route('/user/< username >')  
  def show_user(username):

- How do you collect data from the query string using Flask?
  * request.args["searchterm"]

- How do you collect data from the body of the request using Flask?
  * request.data or request.form (for incoming post forms)

- What is a cookie and what kinds of things are they commonly used for?
  * Way of storing small bits of info on the browser. They are name/string-value pairs. They are used for non-secret information about the browser or info that needs to have a certain expiration time. 

- What is the session object in Flask?
  * Dictionary of encoded information about the current browser that can beused to store information.

- What does Flask's `jsonify()` do?
  * Returns a response in a json object.
