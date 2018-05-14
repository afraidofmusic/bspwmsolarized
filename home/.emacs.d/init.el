;; Melpa ;;
(require 'package)
(add-to-list 'package-archives
             '("melpa-stable" . "https://stable.melpa.org/packages/"))
(package-initialize)
;; Melpa ;;

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   (quote
    ("8db4b03b9ae654d4a57804286eb3e332725c84d7cdab38463cb6b97d5762ad26" default)))
 '(frame-background-mode (quote dark))
 '(fringe-mode 0 nil (fringe))
 '(linum-format "%3d ")
 '(menu-bar-mode nil)
 '(package-selected-packages
   (quote
    (org-bullets writeroom-mode powerline py-autopep8 flycheck dashboard elpy)))
 '(scroll-bar-mode nil)
 '(tool-bar-mode nil)
 '(writeroom-major-modes (quote (text-mode org-mode)))
 '(writeroom-width 100))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:height 117 :family "Iosevka"))))
 '(linum ((t (:background "#eee8d5")))))

;; Solarized
(add-to-list 'custom-theme-load-path "~/.emacs.d/emacs-color-theme-solarized")
(set-frame-parameter nil 'background-mode 'light)
(set-terminal-parameter nil 'background-mode 'light)
(load-theme 'solarized)
;; Solarized

;; Powerline
(powerline-default-theme)
;; Powerline

;; Keybinds
(global-set-key (kbd "C-c l") 'linum-mode)
(global-set-key (kbd "C-c h") 'hl-line-mode)
(global-set-key (kbd "C-c w") 'writeroom-mode)
;; Keybinds

;; Python
(elpy-enable)
(dashboard-setup-startup-hook)
(when (require 'flycheck nil t)
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))
(add-hook 'elpy-mode-hook 'py-autopep8-enable-on-save)
(setq elpy-rpc-python-command "python3")
;; Python

(add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))