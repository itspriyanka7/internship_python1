<!-- ################## Document Object Model. ###################3 -->

# What is Dom?

- The Document Object Model (DOM) is a programming interface for web documents.

- It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.

-   - console.log(window.document); // Human readable representation of JS
    - console.dir(window.document); // JS Object what Browers See.

- With help of Document Object we can Make many Changes 

 # Why DOM is required?

- HTML is used to structure the web pages and Javascript is used to add behavior to our web pages.
 When an HTML file is loaded into the browser, the javascript can not understand the HTML 
 document directly. So, a corresponding document is created(DOM). DOM is basically the 
 representation of the same HTML document but in a different format with the use of objects. 
 Javascript interprets DOM easily i.e javascript can not understand the tags(<h1>H</h1>) in 
 HTML document but can understand object h1 in DOM. Now, Javascript can access each of the 
 objects (h1, p, etc) by using different functions.

# Structure of DOM: DOM can be thought of as a Tree or Forest(more than one tree). 
The term structure model is sometimes used to describe the tree-like representation of a 
document.  Each branch of the tree ends in a node, and each node contains objects  
Event listeners can be added to nodes and triggered on an occurrence of a given event. 
One important property of DOM structure models is structural isomorphism: if any two DOM
 implementations are used to create a representation of the same document, they will create 
 the same structure model, with precisely the same objects and relationships.


# Why called an Object Model?
-  Documents are modeled using objects, and the model includes not only the structure of a document
 but also the behavior of a document and the objects of which it is composed like tag elements 
 with attributes in HTML.



#  Window Object: Window Object is object of the browser which is always at top of the hierarchy.
    It is like an API that is used to set and access all the properties and methods of the 
    browser. It is automatically created by the browser.

# Document object: When an HTML document is loaded into a window, it becomes a document object. 
 The ‘document’ object has various properties that refer to other objects which allow access 
 to and modification of the content of the web page. If there is a need to access any element 
 in an HTML page, we always start with accessing the ‘document’ object. Document object is 
 property of window object.

# Form Object: It is represented by form tags.
# Link Object: It is represented by link tags.
# Anchor Object: It is represented by a href tags.
# Form Control Elements:: Form can have many control elements such as text fields, buttons, 
  radio buttons, checkboxes, etc.


## Four ways to link JS file
- head  : script src="script.js"
- body  : script src="script.js"
- async : script src="script.js" async
- defer : script src="script.js" defer

<!-- // Async vs Defer --> 
# Async VS Defer
## Correct way to link the JS file : 
  
- If you're working with JavaScript, it's important to understand the difference between async and defer attributes

    <script src="./Async_vs_Defer.js"></script> 
    1. html file will pe parse till here and then Js will start loading , after than it will start executing
    Bur problem with declaring file here is rest html is not parsed and if js is applied in below tags i may throw error so its bad practice 

    2. Declaring js file here  : file is been read from top to bottom so html content and css will be parsed and loaded ,
       as it reaches here Js file starts to load after it the file will be executed this process is good less chances of error but 
       its very time comsuming .

    <script src="./Async_vs_Defer.js" async></script>  
    3. Async Way of Linking : So when Browser gets file It starts Read file from top and when it reaches JS file script as we have used async - i.e
      asynchronous attribute so parsing of html and loading of JS file occurs at same time 
      Problem here is lets consider JS file is loaded fully but Html is parsed half way through file as soon as Js is Loaded html parsing will stop and 
      JS file Execution will start with half parsed html file which may cause and error if JS is used below ,So this approach is also not that efficient.
     
    <script src="./Async_vs_Defer.js" defer></script> 
    4. Best way to Link JS file  : Defer (Deferred) So here File reading Start from top as it reach script the loading of script file and parsing of html
       occurs at same time lets say js file is loaded completely so here in case of defer html parsing doesnt stop it continues till its full loaded and that loaded 
      Js file is on hold as both html and js are loaded now execution of script occurs with error and this is best approach as saves time as well. 

### Asynchronous	

  - Asynchronous blocks the parsing of the page.	
  - Asynchronous scripts don’t wait for each other. 
  - The execution of scripts begins by pause parsing.	

### Deferred
  
  - Deferred never blocks the page.
  - Deferred scripts maintain their relative order which means the first script will be loaded first while all others below it will have to wait.
  - However, the execution of scripts begins only after parsing is completely finished but before the document’s DOMContentLoadedevent.
