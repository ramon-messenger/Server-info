# Define the path to your file
$filePath = "C:\Users\AB31581\OneDrive - Lumen\Documents\SRE\Code_Development\server-info\all.hostname.vcenter.txt"

# Read the data from the file
$data = Get-Content -Path $filePath

# Initialize an empty array to hold the output objects
$output = @()

# Loop over the lines
for ($i = 0; $i -lt $data.Count; $i += 2) {
    # Create a new object with the hostname and vcenter
    $obj = New-Object PSObject -Property @{
        Hostname = ($data[$i] -split ":")[1].Trim()
        VCenter  = if ($i + 1 -lt $data.Count) { ($data[$i + 1] -split ":")[1].Trim() } else { $null }
    }

    # Add the object to the output array
    $output += $obj
}

# Display the output
$output | Format-Table
