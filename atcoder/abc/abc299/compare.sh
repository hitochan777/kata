while true; do
    python E_gen.py > test
    ans1=$(python E.py < test)
    ans2=$(python E_naive.py < test)
    echo $ans1
    echo $ans2
    if [ "$ans1" != "$ans2" ]; then
        echo "Wrong Answer"
        echo $ans1
        echo $ans2
        exit
    fi
done