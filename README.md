# Vim-Fanfou
Fanfou is a Twitter clone. 
Vim-fanfou is a TwitVim clone ( https://github.com/vim-scripts/TwitVim ).
Vim-fanfou allows you to post to status and view Fanfou timeline.

# Installation
 - Requirements:   
   Vim-Fanfou is based on Python 2.7(+) & VIM 7+.
   Please check your VIM before you install Vim-Fanfou.
 - Steps to install:   
   Copy the "plugin" folder to your VIM "plugin" folder.

# Usage
## Setup & Login
 - To enable HTTP Proxy: Add below line to your .vimrc.    
   `let g:fanfou_http_proxy = "http://<proxy-host>:<proxy-port>"`
 - To setup your Fanfou account: Run below command for save the Fanfou OAuth token.   
   `:FanfouSetAccount`    
   - This command will open the Fanfou OAuth confirmation Web Page.
   - After you get the PIN code, please enter it to VIM.   
     NOTE: In default, Vim-Fanfou saves your OAuth Token
         to "$HOME/.fanfou_auth_cache".

## Commands
 - FanfouSetAccount   
   To setup your Fanfou account. Please check "Setup & Login" section.
 - FanfouSwitchAccount   
   To switch another Fanfou account.
 - FanfouHomeTimeline   
   To update your Fanfou Home timeline in a Vim Buffer.
 - FanfouRefresh   
   To update Fanfou Vim Buffer.
 - FanfouPostStatus    
   To post a new Status to your Fanfou.

## Shortcut key
 - To update your Fanfou Vim Buffer:   
   `nnoremap <buffer> <silent> <Leader><Leader> :FanfouRefresh`

# License
Vim-fanfou is distributed under the same terms as VIM itself. See :help license.

# Contact
 - The maintainer: @Xiongjia_Le ( http://fanfou.com/xiongjia_le ) 
