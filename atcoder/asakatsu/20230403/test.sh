while true; do
    python E_gen.py > input.txt
    ans1=$(python E.py < input.txt)
    ans2=$(python E_naive.py < input.txt)
    if [ $ans1 != $ans2 ]; then
        echo "Wrong Answer"
        echo $ans1
        echo $ans2
        exit
    fi
done