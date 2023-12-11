#!/bin/bash

if [ $# -gt 0 ]; then
	full_filename="${1}.sh"
	echo "#!/bin/bash" > "${full_filename}"
	chmod +x "${full_filename}"
	subl "$full_filename"
else
	echo "No name_file provided!"
fi