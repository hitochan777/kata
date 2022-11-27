
while true; do
    python F_gen.py > input.txt
    ans1=$(python F.py < input.txt > ans1)
    ans2=$(python F_2.py < input.txt > ans2)
    if ! diff ans1 ans2; then
        exit
    fi
done