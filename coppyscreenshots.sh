python3 ~/Documents/Scripts/coppyScreenshots.py 
cp -r -n ~/.minecraft/screenshots/* ~/Dropbox/Minecraft_Screenshots
cp -r -n ~/.minecraft2/screenshots/* ~/Dropbox/Minecraft_Screenshots
cp -r -n ~/.minecraft3/screenshots/* ~/Dropbox/Minecraft_Screenshots
cp -r -n ~/.minecraft4/screenshots/* ~/Dropbox/Minecraft_Screenshots

rm -r ~/.minecraft/resourcepacks/NathanResourcePack/
rm -r ~/.minecraft3/resourcepacks/NathanResourcePack/
rm -r ~/.minecraft4/resourcepacks/NathanResourcePack/

cp -r -n ~/Dropbox/NathanResourcePack/ ~/.minecraft/resourcepacks/
cp -r -n ~/Dropbox/NathanResourcePack/ ~/.minecraft3/resourcepacks/
cp -r -n ~/Dropbox/NathanResourcePack/ ~/.minecraft4/resourcepacks/

rm ~/.minecraft3/resourcepacks/NathanResourcePack/assets/minecraft/textures/blocks/glass.png
rm ~/.minecraft4/resourcepacks/NathanResourcePack/assets/minecraft/textures/blocks/glass.png

