2. tree -d -L 2 ~
3. mkdir etc
cd etc
5. ls -a
6. cd ~
mkdir structure
7. 8. 9. 10. cd structure
mkdir structure
cd structure
mkdir {2020..2023}
cd 2018
mkdir files
mkdir pictures
mkdir .passwords
cd files
touch data.md
cd ~
cd structure/2018/pictures
touch picture.png
cd ~
cd structure/2018/.passwords
touch .passwords.txt
cd ~
cd structure
cp -rT 2018 2019
cp -rT 2018 2020
cp -rT 2018 2021
cp -rT 2018 2022
cp -rT 2018 2023
11. cd 2018
touch -at 202401010000 data.md
cd ~
cd structure/2019/files
touch -at 202401010000 data.md
cd ~
cd structure/2020/files
touch -at 202401010000 data.md
cd ~
cd structure/2021/files
touch -at 202401010000 data.md
cd ~
cd structure/2021/files
touch -at 202401010000 data.md
cd ~
cd structure/2022/files
touch -at 202401010000 data.md
cd ~
cd structure/2023/files
touch -at 202401010000 data.md
12. cd ~
cd structure/2018/.passwords
touch -mt 201810060000 .passwords.txt 
cd ~
cd structure/2019/.passwords
touch -mt 201910060000 .passwords.txt 
cd ~
cd structure/2020/.passwords
touch -mt 202010060000 .passwords.txt 
cd ~
cd structure/2021/.passwords
touch -mt 202110060000 .passwords.txt 
cd ~
cd structure/2022/.passwords
touch -mt 202210060000 .passwords.txt
cd ~
cd structure/2023/.passwords
touch -mt 202310060000 .passwords.txt 
13. cd ~
cp -R ~/structure/2023 ~/Downloads/2025
14. cd Downloads/2025/.passwords
touch -mt 205210060000 .passwords.txt
15. cd ~
cp -R Downloads/2025 ~/structure
16. cd structure
mv 2025 2024
17. mv 2018/pictures/picture.png 2018/pictures/image.png
mv 2019/pictures/picture.png 2019/pictures/image.png
mv 2020/pictures/picture.png 2020/pictures/image.png
mv 2021/pictures/picture.png 2021/pictures/image.png
mv 2022/pictures/picture.png 2022/pictures/image.png
mv 2023/pictures/picture.png 2023/pictures/image.png
mv 2024/pictures/picture.png 2024/pictures/image.png
18. cd ~
mv structure/2018 Documents
mv structure/2024 Documents
19. cd Documents
rmdir 2024
20. rm -r 2024
21. cd structure/2019/files
cat > data.md
hello
words
ctrl^d
22. cd ~
cd structure/2020/files
nano data.md
23. cd ~/structure/2021/files
code data.md
24. cd ~/structure/2022/files
cat > data.md
hello
words
25. cd ~/structure
mkdir soft_links
mkdir hard_links
26. cd soft_links
n -s ~/structure/2019 2019
n -s ~/structure/2020 2020
n -s ~/structure/2021 2021
n -s ~/structure/2022 2022
n -s ~/structure/2023 2023
27. cd ~/structure/hard_links
ln ~/structure/2020/files/data.md data_2020
ln  ~/structure/2021/.passwords/.passwords.txt passwords_2021
28. cd ~/structure
mkdir archives
30. cd ~
mv Downloads/image.jpg structure/archives
31. cd structure/archives
tar -cvf image.tar image.jpg
tar -cvzf image.tar.gz image.jpg
tar -cvjf image.tar.bz2 image.jpg
32. cd ~
zip -er structure.zip structure
