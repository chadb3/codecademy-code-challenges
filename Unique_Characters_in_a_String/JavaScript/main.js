// if the string has duplicates characters return false
// if the string has no duplicate characters return true
// if string is empty then return \"Error\"
const unique_characters=(string_in)=>
{
 if(string_in.length===0){return "Error";}
 let len=string_in.length;
// console.log(string_in.length);
 for(let i=0;i<len;i++)
 {
  //console.log(string_in[i]);
  for(let j=0;j<len;j++)
  {
    if(i!==j && string_in[i]===string_in[j])
    {
      return false;
    }
  }
 }
/* for(chr of string_in)
 {
  console.log(chr);
 }*/
return true;
}
console.log("Unique Characters in a String?");
console.log(unique_characters("HELP"));
console.log(unique_characters("Hello"));
console.log(unique_characters("test"));
console.log(unique_characters(""));
