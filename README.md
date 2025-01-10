CommandLine Utitlity for Uncryption- Encryption and Decryption but very unoptimized and much worse.
Made as a school project. <br> The code is extremely ugly because of the restrictions placed on us.
# Usage 
1. Clone the Repo into a suitable location and `cd` into it
2. run `python main.py -[mode] -[algorithm] [path of input file] [path of output file] [key(optional, depending on algorithm chosen)]`

> **NOTE:** The output file will completely be overwritten with the encrypted/decrypted data. It is therefore reccomended to use an empty file for dumping the output.

> **NOTE:** If the output file does not exist already, the program will create a new file with the name provided and dump the output there.

> **NOTE:** Merely the name of the file(s) will suffice if the file(s) reside(s) in the same directory as `main.py`. Otherwise, the complete paths of the file(s) is/are requried.

As of now, only Caeser Cipher and some of its derivative algorithms (such as the August and ROT-13 ciphers) are supported.
<br>All flags types, along with thier possible flags are described breifly below-<br>
<table>
  <tr> 
   <th>Flag Type</th>
   <th>Description</th>
   <th>Possible Flags</th>
   <th>Description</th>
  </tr>
  <tr>
    <td rowspan="2">-[mode]</td>
    <td rowspan="2">Specifies the 'mode' of execution. That is, if the script is going to be used for encryption or decryption</td>
    <td>-e</td>
    <td>Specifies that the script is going to be used for the pourposes of encryption</td>
  </tr>
  <tr>
    <td>-d</td>
    <td>Specifies that the script is going to be used for the pourposes of decryption</td>
  </tr>
  <tr>
    <td rowspan="3">-[algorithm]</td>
    <td rowspan="3">Specifies the algorithm to be used for cryptography</td>
    <td>-c</td>
    <td>Specifies that Caesar Cipher is going to be used for cryptography</td>
  </tr>
  <tr>
    <td>-r13</td>
    <td>Specifies that ROT-13 is going to be used for cryptography</td>
  </tr>
  
  <tr>
    <td>-a</td>
    <td>Specifies that August Cipher is going to be used for cryptography</td>
  </tr>
</table>
