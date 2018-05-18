## Load Autoconfig
config.load_autoconfig()
## Colors
c.colors.completion.category.bg = '#657b83'
c.colors.completion.category.border.bottom = '#657b83'
c.colors.completion.category.border.top = '#657b83'
c.colors.completion.category.fg = '#fdf6e3'
c.colors.completion.even.bg = '#eee8d5'
c.colors.completion.fg = '#657b83'
c.colors.completion.item.selected.bg = '#657b83'
c.colors.completion.item.selected.border.bottom = '#657b83'
c.colors.completion.item.selected.border.top = '#657b83'
c.colors.completion.item.selected.fg = '#fdf6e3'
c.colors.completion.match.fg = '#d33682'
c.colors.completion.odd.bg = '#fdf6e3'
c.colors.completion.scrollbar.bg = '#073642'
c.colors.completion.scrollbar.fg = '#586e75'
c.colors.downloads.bar.bg = '#657b83'
c.colors.downloads.error.bg = '#dc322f'
c.colors.downloads.error.fg = '#eee8d5'
c.colors.downloads.start.bg = '#268bd2'
c.colors.downloads.start.fg = '#eee8d5'
c.colors.downloads.stop.bg = '#859900'
c.colors.downloads.stop.fg = '#eee8d5'
c.colors.hints.bg = '#657b83'
c.colors.hints.fg = '#002b36'
c.colors.hints.match.fg = '#fdf6e3'
c.colors.messages.error.bg = '#fdf6e3'
c.colors.messages.error.border = '#fdf6e3'
c.colors.messages.error.fg = '#657b83'
c.colors.messages.info.bg = '#fdf6e3'
c.colors.messages.info.border = '#fdf6e3'
c.colors.messages.info.fg = '#657b83'
c.colors.messages.warning.bg = '#fdf6e3'
c.colors.messages.warning.border = '#fdf6e3'
c.colors.messages.warning.fg = '#657b83'
c.colors.prompts.bg = '#657b83'
c.colors.prompts.border = '5px solid #657b83'
c.colors.prompts.fg = '#fdf6e3'
c.colors.prompts.selected.bg = '#eee8d5'
c.colors.statusbar.command.bg = '#839496'
c.colors.statusbar.command.fg = '#fdf6e3'
c.colors.statusbar.command.private.bg = '#839496'
c.colors.statusbar.command.private.fg = '#fdf6e3'
c.colors.statusbar.insert.bg = '#839496'
c.colors.statusbar.insert.fg = '#fdf6e3'
c.colors.statusbar.normal.bg = '#839496'
c.colors.statusbar.normal.fg = '#fdf6e3'
c.colors.statusbar.private.bg = '#839496'
c.colors.statusbar.private.fg = '#fdf6e3'
c.colors.statusbar.progress.bg = '#fdf6e3'
c.colors.statusbar.url.error.fg = '#fdf6e3'
c.colors.statusbar.url.fg = '#fdf6e3'
c.colors.statusbar.url.hover.fg = '#fdf6e3'
c.colors.statusbar.url.success.http.fg = '#fdf6e3'
c.colors.statusbar.url.success.https.fg = '#fdf6e3'
c.colors.statusbar.url.warn.fg = '#fdf6e3'
c.colors.tabs.bar.bg = '#fdf6e3'
c.colors.tabs.even.bg = '#fdf6e3'
c.colors.tabs.even.fg = '#657b83'
c.colors.tabs.odd.bg = '#fdf6e3'
c.colors.tabs.odd.fg = '#657b83'
c.colors.tabs.selected.even.bg = '#657b83'
c.colors.tabs.selected.even.fg = '#eee8d5'
c.colors.tabs.selected.odd.bg = '#657b83'
c.colors.tabs.selected.odd.fg = '#eee8d5'
## Fonts
c.fonts.completion.category = "bold 12pt Roboto Condensed"
c.fonts.completion.entry = "12pt Roboto Condensed"
c.fonts.debug_console = "12pt Roboto Condensed"
c.fonts.downloads = "12pt Roboto Condensed"
c.fonts.keyhint = "12pt Roboto Condensed"
c.fonts.messages.error = "12pt Roboto Condensed"
c.fonts.messages.info = "12pt Roboto Condensed"
c.fonts.messages.warning = "12pt Roboto Condensed"
c.fonts.monospace = "Iosevka"
c.fonts.prompts = "12pt Roboto Condensed"
c.fonts.statusbar = "12pt Roboto Condensed"
c.fonts.tabs = "12pt Roboto Condensed"
c.fonts.web.family.cursive = "Roboto Condensed"
c.fonts.web.family.fantasy = "Roboto Condensed"
c.fonts.web.family.fixed = "Iosevka"
c.fonts.web.family.sans_serif = "Roboto Condensed"
c.fonts.web.family.serif = "Roboto Condensed"
c.fonts.web.family.standard = "Roboto Condensed"
c.fonts.web.size.default = 15
c.fonts.web.size.default_fixed = 15
## Hints
c.hints.border = "2px solid #00E3BE23"
c.hints.chars = "asdfghjklqwertyuopzxcvbnm"
c.hints.mode = "letter"
c.hints.scatter = True
## Prompt
c.prompt.filebrowser = True
c.prompt.radius = 0
## Statusbar
c.statusbar.hide = False
c.statusbar.padding = {"bottom": 10, "left": 10, "right": 10, "top": 10}
c.statusbar.widgets = ["keypress", "progress", "url"]
## Tabs
c.tabs.background = True
c.tabs.favicons.show = False
c.tabs.indicator.padding = {"bottom": 2, "left": 0, "right": 4, "top": 2}
c.tabs.indicator.width = 0
c.tabs.padding = {"bottom": 10, "left": 10, "right": 10, "top": 10}
c.tabs.pinned.shrink = False
c.tabs.position = "top"
c.tabs.show = "always"
c.tabs.title.alignment = "center"
c.tabs.title.format = "{private}{perc}{title}"
c.tabs.title.format_pinned = "Pinned | {title}"
## Completion
c.completion.cmd_history_max_items = 0
c.completion.height = "33%"
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 0
c.completion.shrink = True
c.completion.web_history_max_items = 0
## Search Engines
c.url.searchengines = {"DEFAULT": "https://duckduckgo.com/?q={}", "4c": "https://4chan.org/{}/catalog", "gen": "https://genius.com/search?q={}", "r": "https://reddit.com/r/{}", "tpb": "https://thepiratebay.org/search/{}"}
## Misc
c.confirm_quit = ["multiple-tabs", "downloads"]
c.content.user_stylesheets = ["~/.config/qutebrowser/style.css"]
c.editor.command = ["alacritty", "-e", "vim", "{file}"]
c.url.default_page = "~/.config/qutebrowser/start/start.html"
c.url.start_pages = "~/.config/qutebrowser/start/start.html"
## Keybinds
# Unbind Keys
config.unbind('d', mode='normal')
config.unbind('gl', mode='normal')
config.unbind('gr', mode='normal')
config.unbind('J', mode='normal')
config.unbind('K', mode='normal')

config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('dd', 'tab-close')
config.bind('gj', 'tab-move -')
config.bind('gk', 'tab-move +')
config.bind('ZZ', 'config-cycle tabs.show always never')
config.bind('zz', 'config-cycle statusbar.hide true false')
