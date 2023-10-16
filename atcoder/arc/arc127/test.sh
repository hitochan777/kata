while true; do
    python A_random.py > input.txt
    ans1=$(python A.py < input.txt)
    ans2=$(python A_test.py < input.txt)
    if [ $ans1 != $ans2 ]; then
        echo "Wrong Answer"
        echo $ans1
        echo $ans2
        exit
    fi
done