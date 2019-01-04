##VGM Utils
A series of python scripts intended to simplify working with vgm and vgz files.
Tools should be cross-platform and relatively user-friendly. Should include libraries and also command line interfaces

####Road Map and Ideas
 - [x] Tool for conversion between `.vgm.gz` to `.vgz` and vice versa. see: `vgmgz2vgz.py` & `vgz2vgmgz.py`
   - [ ] Add `argparse` argument for directory to change.
   - [ ] Add `argparse` argument for preview change.
 - [ ] Tool for extracting Dexed (dx7) configurations from instruments within compatible VGM files.
 - [ ] Library for fetching metadata. (tags, statistics) Should also consider allowing additional unsupported tags (replaygain, genre, mood) to be appended to files as APETAG footers. This will be basis for better Quodlibet implementation.
 - [ ] Tool for extracting samples (or wavetables) from individual vgm files.
   - [ ] Sega Genesis / Mega Drive `PCM` > `.wav`
   - [ ] NES `PCM` > `.wav`
 - [ ] Tool for unpacking `.vgz` files (`vgz` => `vgm`) and vice verse. Difficulty of this will be to achieve cross-platform support.
