while true; do
    echo "yeah"
    python D_random.py > input.txt
    ans1=$(python D.py < input.txt)
    ans2=$(python D_n.py < input.txt)
    if [ $ans1 != $ans2 ]; then
        echo "Wrong Answer"
        echo $ans1
        echo $ans2
        exit
    fi
done