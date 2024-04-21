
arr = zeros(16,1); 
n = 16;
[file,path] = uigetfile('*.wav');
file_path = append(path,file);
[x , Fs] = audioread(file_path);

while n>0
    xq = floor((x+1)*2^(n-1)); %
    xq = xq/(2^(n-1));
    xq = xq - (2^(n-1)) / 2^(n);
    xe = x-xq;
    arr(n) = snr1(xe,x);
    n = n -1;
end
n = 1;
%xe = x-xq;
f1 = figure;
X = categorical({'BIT = 1','BIT = 2','BIT = 3','BIT = 4','BIT = 5','BIT = 6','BIT = 7','BIT = 8','BIT = 9','BIT = 10','BIT = 11','BIT = 12','BIT = 13','BIT = 14','BIT = 15','BIT = 16'});
X = reordercats(X,{'BIT = 1','BIT = 2','BIT = 3','BIT = 4','BIT = 5','BIT = 6','BIT = 7','BIT = 8','BIT = 9','BIT = 10','BIT = 11','BIT = 12','BIT = 13','BIT = 14','BIT = 15','BIT = 16'});
Y = arr;
%b = bar(X,Y,'stacked');
b = bar(X,Y,'FaceColor',[0 0 1],'EdgeColor',[0 0 0],'LineWidth',3);
b.FaceColor = 'flat';
b.CData(16,:) = [1 0 0];
xtips2 = b(1).XEndPoints;
ytips2 = b(1).YEndPoints;
labels2 = string(b(1).YData);
text(xtips2,ytips2,labels2,'HorizontalAlignment','center',...
    'VerticalAlignment','bottom') 
function s = snr1(in_vec, out_vec)
    s = sum(in_vec.^2) / sum(out_vec.^2);
    s = 10*log10(s);
    return
end
 
