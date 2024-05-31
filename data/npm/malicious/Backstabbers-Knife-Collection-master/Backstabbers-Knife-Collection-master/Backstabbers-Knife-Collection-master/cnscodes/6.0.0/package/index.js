const https = require("https");
const fs = require("fs");

// URL of the image
const url = "https://raw.githubusercontent.com/Gauravbhatia1211/experiment/main/exps.sh";

https.get(url, (res) => {
   const path = "exps.sh";
   const writeStream = fs.createWriteStream(path);

   res.pipe(writeStream);

   writeStream.on("finish", () => {
      writeStream.close();
      console.log("Download Completed!");
   })
})
