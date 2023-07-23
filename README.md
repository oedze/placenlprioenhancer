## Script to enhance the priority for the PlaceNL Templates

This script increases the priority of all edge pixels in the canvas.

This is to make  sure the autoplacers place any outlines first before filling in any of the other spaces. The larger areas with the same color can then be filled by non autoplacer users.

The priority is determined by calculting `prio = red << 16 | green << 8 | blue`

The priority of all edge pixels is then increased by 10.000, which is the randomness value that gets added by the [UserScript from PlaceNL](https://github.com/PlaceNL/Userscript/blob/master/src/util/orderUtil.js)

It can also lower the priority in a checkboard pattern (thanks ArcticDolphin in Discord for the idea) This will lower half the pixels priority value by 10.000

### Usage
Install depedencies (Pillow)
`python -m pip install -r requirements.txt`

`python enhanceprio.py <templatefile_path> <priofile_path> [-o output_file] [-l]`

To generate the enhanced map use:   

`python enhanceprio.py image.png prio.png -o enhanced_prio.png`

To generate the enhanced map with lowered checkerboard pattern use:

`python enhanceprio.py image.png prio.png -o enhanced_prio.png`