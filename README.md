CommandLine Utitlity for Uncryption- Encryption and Decryption but very unoptimized and much worse.
Made as a school project. <br> The code is extremely ugly because of the restrictions placed on us.
#<br><h><b>Usage</b></h><br>
<ol>
  <li>Clone the Repo into a suitable location and `cd` into it</li>
  <li>run `python main.py -[mode] -[algorithm] [message] [key(optional, depending on algorithm chosen)]`</li>
</ol>
As of now, only Caeser Cipher and some of its derivative algorithms (such as the August and ROT-13 ciphers) are supported.
The flags may be used as follows
<table>
  <tr>
    <th>Flag Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td> `-[mode]` </td>
    <td>Specifies the 'mode' of execution. That is, if the script is going to be used for encryption or decryption</td>
  </tr>
  <tr>
    <td>`-[algorithm]`</td>
    <td>Specifies the algorithm to be used for encryption/decryption</td>
  </tr>  
</table>
The various possible flags for each flag type is given as follows-
<table>
  <tr> 
   <th>Flag Type</th>
   <th>Possible Flags</th>
   <th>Description</th>
  </tr>
  <tr>
    <td rowspan="2">` -[mode] `</td>
    <td>`-e`</td>
    <td>Specifies that the script is going to be used for the pourposes of encryption</td>
  </tr>
  <tr>
    <td>`-d`</td>
    <td>Specifies that the script is going to be used for the pourposes of decryption</td>
  </tr>
  <tr>
    <td rowspan="3">` -[algorithm] `</td>
    <td>`-c`</td>
    <td>Specifies that Caesar Cipher is going to be used for cryptography</td>
  </tr>
  <tr>
    <td>`-r13`</td>
    <td>Specifies that ROT-13 is going to be used for cryptography</td>
  </tr>
  
  <tr>
    <td>`-a`</td>
    <td>Specifies that August Cipher is going to be used for cryptography</td>
  </tr>
</table>
