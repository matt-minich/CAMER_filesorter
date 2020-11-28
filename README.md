# CAMER_filesorter
This script was designed to help researchers save time when sorting through the CAMER Twitter data. 

That dataset contains a unique file for each three-hour block within each day. However, if the volume of tweets captured during that period exceeded Synthesio's 50k cap, the data for that period was resampled using a different method (10% of total volume) and saved as a separate file. When preparing the data for analysis, it's important to identify which time periods have been resampled and replace the original files with the resampled files. This can be a bit of a pain. 

This script renames the files in a way that makes it easy. To use it, follow these steps:

1. Change the path in line 7 to the directory where you are storing your Twitter data. 
2. Create four folders in that directory: "Original", "Resampled", "Output" and "Script".
3. Save the script in the "Script" folder.
4. Drop the originally-sampled tweets into the "Original" folder. Those are the first files in any folder. 
5. If you have files labeled "after_resampling", drop them into the "Resampled" folder. 
6. Just run the script! 

If you have any trouble just email mminich@wisc.edu.
