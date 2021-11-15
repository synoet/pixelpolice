files=`find ~/dev/cox/dri-frontend/packages/consumer-checkout -regex '.*/***/[^/]*styles.ts'`

for file in $files
do
  echo "----------------"
  echo "File: $file"
  output=$(python main.py $file --count-culprits 2>&1)
  culprits=$(python main.py $file --culprits 2>&1)
  echo "Number of Lines with broken rules: $output"
  echo "Culprits: $culprits"
  echo "----------------"
  echo " "
done
 
