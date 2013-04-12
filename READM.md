

# Sublime Auto Bookmark

A Sublime plugin to auto bookmark based on a string given.

Then provides a list of bookmarks for easy navigation.

Similar to [Dog Ears](https://github.com/skyronic/DogEars) but using the lines actual text instead of an input.


## Sample Windows key-bindings 

	{ "keys":["ctrl+shift+f"], "command": "bookmark_containing" },
	{ "keys":["ctrl+shift+b"], "command":"browse_auto_bookmarks" },
	{ "keys":["ctrl+shift+a"], "command":"auto_bookmark" },

## Usage

### Commands:

+ 	**bookmark_containing** 
	
	input string that matches lines you want to bookmark

	ex. /***
		/*BOOKMARK*/
		etc.

+ 	**browse\_auto\_bookmarks** 

	lists all bookmarks
	
	clicking one item will scroll your file to the bookmark selected

+	**auto_bookmark** 
	
	automatically adds bookmarks using /** as the string that matches lines that will be bookmarked

	*this is what i use on my less/css files :p free to change the default string*

