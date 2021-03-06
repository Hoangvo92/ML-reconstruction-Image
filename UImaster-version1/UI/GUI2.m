function varargout = GUI2(varargin)
% GUI2 MATLAB code for GUI2.fig
%      GUI2, by itself, creates a new GUI2 or raises the existing
%      singleton*.
%
%      H = GUI2 returns the handle to a new GUI2 or the handle to
%      the existing singleton*.
%
%      GUI2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUI2.M with the given input arguments.
%
%      GUI2('Property','Value',...) creates a new GUI2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before GUI2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to GUI2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GUI2

% Last Modified by GUIDE v2.5 17-Nov-2021 22:49:48

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GUI2_OpeningFcn, ...
                   'gui_OutputFcn',  @GUI2_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before GUI2 is made visible.
function GUI2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to GUI2 (see VARARGIN)

% Choose default command line output for GUI2
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes GUI2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);
%handles.num_e = 0;
handles.E = [];
%setappdata(handles.E, 'E', []);
%setappdata(handles.num_e, 'num_e', 0);
%guidata(hObject, handles);
setappdata(0, 'E', []);
setappdata(0  , 'GUI2'    , gcf);
%setappdata(gcf,   'GUI3'    , 121);
setappdata(gcf, 'updateE', @updateE);

% --- Outputs from this function are returned to the command line.
function varargout = GUI2_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in B2_1.
function B2_1_Callback(hObject, eventdata, handles)
% hObject    handle to B2_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
     GUI3;
 %    rowE = handles.rowE;
  %   E = handles.E;
  %   E = [E; rowE];
 %    num_E = height(E);
 %    handles.num_e = num_E;
 %    handles.E = E;
 %    set(handles.edit1, 'String', string(num_E));
    % guidata(hObject, handles);
function updateE

Gui2 = getappdata(0, 'GUI2');
%fileName = getappdata(Gui2, 'fileName');
%Gui3   = getappdata(Gui2, 'GUI3');
ellipse = getappdata(0, 'E');
rowE = getappdata(0, 'rowE');
ellipse = [ellipse; rowE];
num_E = height(ellipse);
setappdata(Gui2, 'E', ellipse);
edit1 = findobj(Gui2, 'tag', 'edit1');
set(edit1, 'String', string(num_E));

%    ellipse = getappdata(handles.GUI2,'E');
%    ellipse = [ellipse; rowE];
%    num_E = height(E);
%    setappdata(handles.GUI2, "num_e", num_E);%handles.num_e = num_E;
%    setappdata(handles.GUI2, 'E', ellipse);%handles.E = E;
%    set(handles.edit1, 'String', string(num_E));
%    guidata(hObject,handles);


% --- Executes on button press in B2_2.
function B2_2_Callback(hObject, eventdata, handles)
% hObject    handle to B2_2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
   E = getappdata(0, "E");
   E(end,:) = [];
   num_E = height(E);
   handles.num_e = num_E;
   handles.E = E;
   set(handles.edit1, 'String', string(num_E));
   guidata(hObject, handles);
   setappdata(0, "E", E);

% --- Executes on button press in B2_3.
function B2_3_Callback(hObject, eventdata, handles)
% hObject    handle to B2_3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
    E = getappdata(0, 'E');
    P1 =  mriphantom(E, 500);
    axes(getappdata(0, 'axes2'));
    imshow(P1);
    P2 = imt1phantom(E, 500);
    axes(getappdata(0, 'axes1'));
   % axes(handles.axes1);
    imshow(P2);
    P3 = imt2phantom(E, 500);
    axes(getappdata(0, 'axes3'));
    imshow(P3);
    setappdata(0, 'P1', P1);
    setappdata(0, 'P2', P2);
    setappdata(0, 'P3', P3);
    guidata(hObject,handles);
    closereq();


function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
