OPENNP="\001"
CLOSENP="\002"
bold_green="${OPENNP}\033[1;32m${CLOSENP}"
bold_red="${OPENNP}\033[1;31m${CLOSENP}"
blue="${OPENNP}\033[0;94m${CLOSENP}"
grey="${OPENNP}\033[0;90m${CLOSENP}"

reset="${OPENNP}\033[0m${CLOSENP}"



function show_status {
    if [ $RETVAL == 0 ]
    then
        echo -e "${bold_green}✓${reset}"
    else
        echo -e "${bold_red}✕${reset}"
    fi
}


function build_prompt {
    RETVAL=$?
    
    PS1X=$([[ "$PWD" =~ ^"$HOME".* ]] && echo ${PWD/$HOME/'~'} || echo $PWD)   
    PROMPT="${bold_green}${USER}${reset}:${blue}${PS1X}${reset}${grey}"
    echo -ne $PROMPT

    RPROMPT=$(date +%T)
    echo -ne "\033[${COLUMNS}C\033[$((${#RPROMPT}-1))D${RPROMPT}"

    echo -e "\n$(show_status)"
}


export PS1="\`build_prompt\`> "
