for x in {36..72..2}; do tshark -Tfields -e data -r otherplane.data frame.number==$x | python3 -c "print(__import__('binascii').unhexlify(input()).decode('utf-8'), end='')"; done
