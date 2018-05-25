### Solarized
solarized = {
        'base03': '#002b36',
        'base02': '#073642',
        'base01': '#586e75',
        'base00': '#657b83',
        'base0': '#839496',
        'base1': '#93a1a1',
        'base2': '#eee8d5',
        'base3': '#fdf6e3',
        'yellow': '#b58900',
        'orange': '#cb4b16',
        'red': '#dc322f',
        'magenta': '#d33682',
        'violet': '#6c71c4',
        'blue': '#268bd2',
        'cyan': '#2aa198',
        'green': '#859900'
}
## Colors
c.colors.completion.category.bg = solarized['base00']
c.colors.completion.category.border.bottom = solarized['base00']
c.colors.completion.category.border.top = solarized['base00']
c.colors.completion.category.fg = solarized['base3']
c.colors.completion.even.bg = solarized['base2']
c.colors.completion.fg = solarized['base00']
c.colors.completion.item.selected.bg = solarized['base00']
c.colors.completion.item.selected.border.bottom = solarized['base00']
c.colors.completion.item.selected.border.top = solarized['base00']
c.colors.completion.item.selected.fg = solarized['base3']
c.colors.completion.match.fg = solarized['red']
c.colors.completion.odd.bg = solarized['base3']
c.colors.completion.scrollbar.bg = solarized['base02']
c.colors.completion.scrollbar.fg = solarized['base01']
c.colors.downloads.bar.bg = solarized['base00']
c.colors.downloads.error.bg = '#dc322f'
c.colors.downloads.error.fg = solarized['base2']
c.colors.downloads.start.bg = solarized['blue']
c.colors.downloads.start.fg = solarized['base2']
c.colors.downloads.stop.bg = solarized['green']
c.colors.downloads.stop.fg = solarized['base2']
c.colors.hints.bg = solarized['base00']
c.colors.hints.fg = solarized['base03']
c.colors.hints.match.fg = solarized['base3']
c.colors.messages.error.bg = solarized['base3']
c.colors.messages.error.border = solarized['base3']
c.colors.messages.error.fg = solarized['base00']
c.colors.messages.info.bg = solarized['base3']
c.colors.messages.info.border = solarized['base3']
c.colors.messages.info.fg = solarized['base00']
c.colors.messages.warning.bg = solarized['base3']
c.colors.messages.warning.border = solarized['base3']
c.colors.messages.warning.fg = solarized['base00']
c.colors.prompts.bg = solarized['base00']
c.colors.prompts.border = '5px solid #657b83'
c.colors.prompts.fg = solarized['base3']
c.colors.prompts.selected.bg = solarized['base2']
c.colors.statusbar.command.bg = solarized['base0']
c.colors.statusbar.command.fg = solarized['base3']
c.colors.statusbar.command.private.bg = solarized['base0']
c.colors.statusbar.command.private.fg = solarized['base3']
c.colors.statusbar.insert.bg = solarized['base0']
c.colors.statusbar.insert.fg = solarized['base3']
c.colors.statusbar.normal.bg = solarized['base0']
c.colors.statusbar.normal.fg = solarized['base3']
c.colors.statusbar.private.bg = solarized['base0']
c.colors.statusbar.private.fg = solarized['base3']
c.colors.statusbar.progress.bg = solarized['base3']
c.colors.statusbar.url.error.fg = solarized['base3']
c.colors.statusbar.url.fg = solarized['base3']
c.colors.statusbar.url.hover.fg = solarized['base3']
c.colors.statusbar.url.success.http.fg = solarized['base3']
c.colors.statusbar.url.success.https.fg = solarized['base3']
c.colors.statusbar.url.warn.fg = solarized['base3']
c.colors.tabs.bar.bg = solarized['base3']
c.colors.tabs.even.bg = solarized['base3']
c.colors.tabs.even.fg = solarized['base00']
c.colors.tabs.odd.bg = solarized['base3']
c.colors.tabs.odd.fg = solarized['base00']
c.colors.tabs.selected.even.bg = solarized['base00']
c.colors.tabs.selected.even.fg = solarized['base2']
c.colors.tabs.selected.odd.bg = solarized['base00']
c.colors.tabs.selected.odd.fg = solarized['base2']
### Fonts
c.fonts.completion.category = 'bold 11pt Roboto Condensed'
c.fonts.completion.entry = '11pt Roboto Condensed'
c.fonts.debug_console = '11pt Roboto Condensed'
c.fonts.downloads = '11pt Roboto Condensed'
c.fonts.keyhint = '11pt Roboto Condensed'
c.fonts.messages.error = '11pt Roboto Condensed'
c.fonts.messages.info = '11pt Roboto Condensed'
c.fonts.messages.warning = '11pt Roboto Condensed'
c.fonts.monospace = 'Iosevka'
c.fonts.prompts = '11pt Roboto Condensed'
c.fonts.statusbar = '11pt Roboto Condensed'
c.fonts.tabs = '11pt Roboto Condensed'
c.fonts.web.family.cursive = 'Roboto Condensed'
c.fonts.web.family.fantasy = 'Roboto Condensed'
c.fonts.web.family.fixed = 'Iosevka'
c.fonts.web.family.sans_serif = 'Roboto Condensed'
c.fonts.web.family.serif = 'Roboto Condensed'
c.fonts.web.family.standard = 'Roboto Condensed'
c.fonts.web.size.default = 15
c.fonts.web.size.default_fixed = 15
### Hints
c.hints.border = '2px solid #00E3BE23'
c.hints.chars = 'asdfghjklqwertyuopzxcvbnm'
c.hints.mode = 'letter'
c.hints.scatter = True
### Prompt
c.prompt.filebrowser = True
c.prompt.radius = 5
### Statusbar
c.statusbar.hide = True
c.statusbar.padding = {'bottom': 10, 'left': 10, 'right': 10, 'top': 10}
c.statusbar.widgets = ['keypress', 'progress', 'url']
### Tabs
c.tabs.background = True
c.tabs.favicons.show = 'pinned'
c.tabs.indicator.width = 0
c.tabs.padding = {'bottom': 10, 'left': 14, 'right': 10, 'top': 10}
c.tabs.title.format_pinned = ''
c.tabs.position = 'top'
c.tabs.title.alignment = 'center'
c.tabs.title.format = '{title}'
c.tabs.wrap = False
### Downloads
c.downloads.position = 'bottom'
### Completion
c.completion.cmd_history_max_items = 0
c.completion.height = '33%'
c.completion.shrink = True
c.completion.web_history_max_items = 0
### Window
c.window.title_format = "{private}{title} {perc}"
### Search Engines
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}',
                       '4c': 'https://4chan.org/{}/catalog',
                       'aur': 'https://aur.archlinux.org/?K={}',
                       'aw': 'https://wiki.archlinux.org/?search={}',
                       'gen': 'https://genius.com/search?q={}',
                       'gw': 'https://wiki.gentoo.org/?search={}', 'w':
                       'https://en.wikipedia.org/?search={}',
                       'r': 'https://reddit.com/r/{}',
                       'tpb': 'https://thepiratebay.org/search/{}',
                       'w': 'https://en.wikipedia.org/?search={}',
                       'wtr': 'https://tr.wikipedia.org/?search={}',
                       'yt': 'https://youtube.com/results?search_query={}'}
### Misc
c.confirm_quit = ['multiple-tabs', 'downloads']
c.content.user_stylesheets = ['~/.config/qutebrowser/style.css']
c.editor.command = ['st', '-e', 'vim', '{file}']
c.url.default_page = '~/.config/qutebrowser/start/start.html'
c.url.start_pages = '~/.config/qutebrowser/start/start.html'
### Keybinds
## Unbind Keys
config.unbind('d', mode='normal')
config.unbind('gl', mode='normal')
config.unbind('gr', mode='normal')
## Bind Keys
config.bind('dd', 'tab-close')
config.bind('gk', 'tab-move -')
config.bind('gj', 'tab-move +')
config.bind('ZZ', 'config-cycle tabs.show always never')
config.bind('zz', 'config-cycle statusbar.hide true false')

### Side Tabs
c.tabs.favicons.show = 'always'
c.tabs.position = 'left'
c.tabs.title.format =''
c.tabs.width = 46
c.tabs.title.format_pinned = ''
c.colors.tabs.bar.bg = solarized['base0']
c.colors.tabs.even.bg = solarized['base0']
c.colors.tabs.odd.bg = solarized['base0']
c.colors.tabs.selected.even.bg = solarized['base1']
c.colors.tabs.selected.odd.bg = solarized['base1']
