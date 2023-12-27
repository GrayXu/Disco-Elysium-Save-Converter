# Disco Elysium Save Converter

PC Save Data:
- Path: `C:\Users\XXX\AppData\LocalLow\ZAUM Studio\Disco Elysium\SaveGames`
- Each save file is composed of `savefname.jpg` and `savefname.ntwtft.zip`
  - The zip file includes `savefname.1st.ntwtft.json`, `savefname.2nd.ntwtft.json`, `savefname.FOW.json`, `savefname.ntwtft.lua`, `savefname.states.lua`.

Switch Save Data:
- 32 len uniquename in SaveSlots
- `uniquename.jpg`, `uniquename.json`, `uniquename.zip`
  - The zip file includes `savefname.1st.ntwtft.json`, `savefname.2nd.ntwtft.json`, `savefname.FOW.json`, `savefname.ntwtft.lua`, `savefname.states.lua`.

## usage

```$ python3 disco-elysium-save-converter.py -s "savefname"```  
this cmd will transfer a pc save file `savefname` in `pc_save/` dir to switch version in `switch_save/` dir

```$ python3 disco-elysium-save-converter.py -p "uniquename"```
this cmd will transfer a switch save dir `uniquename` (*like 1aa3383628ec98183457aefd5ab00f6*) in `switch_save/` dir to pc version in `pc_save/` dir

Finally, copy the corresponding files to the PC directory or Switch.