alias gs="git status -s"

function git_directory {
    USAGE="git_directory REPO SUBDIRECTORY"
    repo=$1
    subdir=$2
    dest=`basename $repo .git`
    if [ -z "$repo" ] || [ -z "$subdir" ]; then
        echo $USAGE
        return 1;
    fi

    git clone --depth 1 $repo $dest
    cd $dest
    git filter-branch --prune-empty --subdirectory-filter $subdir HEAD
}
