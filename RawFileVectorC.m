% Matlab script para obtener el raw de un archivo como vector de C

file_in = fopen("file.jpg",'r');
file_out = fopen('Out.txt','w');

cadena = "const uint8_t file[] = {";

caracter = fread(file_in,1,'uint8');
cadena = cadena + "0x" + dec2hex(sum(caracter));

while (~feof(file_in))
    caracter = fread(file_in,1,'uint8');
    cadena = cadena + ", 0x" + dec2hex(sum(caracter));

end

cadena = char(cadena);

for i = 1:1:(size(cadena,2) - 5)
    fprintf(file_out, "%c", cadena(i));
end
fprintf(file_out, "};")

fclose(file_out)
fclose(file_in)

