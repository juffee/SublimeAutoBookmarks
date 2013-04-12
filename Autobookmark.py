import sublime, sublime_plugin


def save_bookmarks(self, bookmarkPrefix ):

	bookmarkIcon = "bookmark" # dot, circle, bookmark, cross
	autobookmarks = []
	# view = self.window.active_view()

	result = self.view.find_all(bookmarkPrefix, sublime.IGNORECASE | sublime.LITERAL)

	for key, val in enumerate(result):
		line = self.view.line(val)
		autobookmarks.append(line)

		lineString = self.view.substr(line)
		print( lineString )

	self.view.add_regions("autobookmarks", autobookmarks, "bookmarks", "bookmark")


class BookmarkContainingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		window.show_input_panel("Bookmark Lines Containing:", "", self.on_done, None, None)
		pass

	def on_done(self, text):

		bookmarkPrefix = text
		
		save_bookmarks(self, bookmarkPrefix)

class AutoBookmarkCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		
		bookmarkPrefix = "/** "
		
		save_bookmarks(self, bookmarkPrefix)

class BrowseAutoBookmarksCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		bookmarkOpts = []
		self.panelKeys = []
		autobookmarks = self.view.get_regions("autobookmarks")

		for key, val in enumerate(autobookmarks):
			line = self.view.line(val)
			lineString = self.view.substr(line)

			print( lineString )

			bookmarkOpts.append( lineString )
			self.panelKeys.append(line)

		window = self.view.window()
		window.show_quick_panel(bookmarkOpts, self.on_bookmark_selected)
	def erase_status(self):
		
		print("erase")
		self.view.erase_status("autobookmarks")

	def on_bookmark_selected(self, idx):

		if(idx == -1):
			print("No bookmark selected. Returning ")
			return

		line = self.panelKeys[idx]
		lineString = self.view.substr(line)

		self.view.erase_status("autobookmarks")
		self.view.set_status("autobookmarks", lineString)

		print(lineString)

		sublime.set_timeout(self.erase_status, 4000)

		self.view.show(line)


