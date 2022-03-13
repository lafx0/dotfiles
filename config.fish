if status is-interactive
    # Commands to run in interactive sessions can go here
    alias cc "clear"
end

if type -q exa
  alias ll "exa -l -g --icons"
  alias lla "ll -a"
  alias llt2 "ll --tree --level=2"
  alias llt3 "ll --tree --level=3"
end

