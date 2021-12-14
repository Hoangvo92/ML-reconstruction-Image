function saveImage( E, index, image, imageName)
    baseFileName = sprintf('%s_%d.png', imageName, index);
    fullFileName = fullfile('output', baseFileName);
    imwrite(image, fullFileName);

    % Create a table with the data and variable names
  %  T = table(TR, TE, alfa, 'VariableNames', { 'TR', 'TE', 'alfa'} );
    T1 = E(1, 7);
    T2 = E(1, 8);
    T2dot = E(1, 10);
    TR = E(1, 11);
    TE = E(1, 12);
    alfa = E(1, 13);
    Ta = table(T1, T2, T2dot, TR, TE, alfa) ;  
    % Write data to text file
    baseTextName = sprintf('%d.txt', index);
    fullTextName = fullfile('output', baseTextName);
    writetable(Ta, fullTextName);
end