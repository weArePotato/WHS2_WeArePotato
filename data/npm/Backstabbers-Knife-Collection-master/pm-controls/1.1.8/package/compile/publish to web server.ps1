Param(
  [string]$DeployPath
)
try{
    
    $BuildFolder = '..\build\client'
   
    robocopy $BuildFolder $DeployPath /E
}
catch
{
    Write-Error $_
    [System.Environment]::Exit(1)
}
