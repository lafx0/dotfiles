import os

print("[*] Configuring tmux ...")
os.system('wget https://raw.githubusercontent.com/lafx0/dotfiles/main/.tmux.conf -O ~/.tmux.conf')
os.system("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm")
os.system("tmux source ~/.tmux.conf")
print("[+] tmux configured! Enjoy :) ")

print("\n[*] Now configuring vim ...")
os.system("wget https://raw.githubusercontent.com/lafx0/dotfiles/main/.vimrc -O ~/.vimrc")
os.system("source ~/.vimrc")
print("[+] vim configured! Enjoy :) ")
