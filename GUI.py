#!/usr/bin/python

'''
    Skeleton code for a GUI application created by using PyQT and PyVTK
'''


import sys
import math
import random
import vtk
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


'''
    The Qt MainWindow class
    A vtk widget and the ui controls will be added to this main window
'''
class MainWindow(Qt.QMainWindow):

    def __init__(self, parent = None):
        Qt.QMainWindow.__init__(self, parent)
        
        ''' Step 1: Initialize the Qt window '''
        self.setWindowTitle("COSC 6344 Visualization- Assignment 5- Hoang Vo")
        self.resize(1000,self.height())
        self.frame = Qt.QFrame() # Create a main window frame to add ui widgets
        self.mainLayout = Qt.QHBoxLayout()  # Set layout - Lines up widgets horizontally
        self.frame.setLayout(self.mainLayout)
        self.setCentralWidget(self.frame)
        
        ''' Step 2: Add a vtk widget to the central widget '''
        # As we use QHBoxLayout, the vtk widget will be automatically moved to the left
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.mainLayout.addWidget(self.vtkWidget)
        
        #Initialize the vtk variables for the visualization tasks
        self.init_vtk_widget()
        
        # Add an object to the rendering window
        # self.add_vtk_object()
        
        ''' Step 3: Add the control panel to the right hand side of the central widget '''
        # Note: To add a widget, we first need to create a widget, then set the layout for it
        self.right_panel_widget = Qt.QWidget() # create a widget
        self.right_panel_layout = Qt.QVBoxLayout() # set layout - lines up the controls vertically
        self.right_panel_widget.setLayout(self.right_panel_layout) #assign the layout to the widget
        self.mainLayout.addWidget(self.right_panel_widget) # now, add it to the central frame
        
        # The controls will be added here
        self.add_controls()
                
        
    '''
        Initialize the vtk variables for the visualization tasks
    '''    
    def init_vtk_widget(self):
        #vtk.vtkObject.GlobalWarningDisplayOff() #Disable vtkOutputWindow - Comment out this line if you want to see the warning/error messages from vtk
        
        # Create the graphics structure. The renderer renders into the render
        # window. The render window interactor captures mouse events and will
        # perform appropriate camera or actor manipulation depending on the
        # nature of the events.
        self.ren = vtk.vtkRenderer() 
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        # The following set the interactor for 2D image style (i.e., no rotation)
       #style = vtk.vtkInteractorStyleImage()
        #self.iren.SetInteractorStyle(style)
        self.ren.SetBackground(0.8,0.8,0.8) # you can change the background color here

        # Start the vtk screen
        self.ren.ResetCamera()
        self.show()
        self.iren.Initialize()
        self.iren.Start()

    '''
        Add QT controls to the control panel in the righ hand size
    '''
    def add_controls(self):
    
        ''' Add a sample group box '''
        groupBox = Qt.QGroupBox("3D Vector Field Visualization") # Use a group box to group controls
        self.groupBox_layout = Qt.QVBoxLayout() #lines up the controls vertically
        groupBox.setLayout(self.groupBox_layout) 
        self.right_panel_layout.addWidget(groupBox)
  
        ''' Add a textfield ( QLineEdit) to show the file path and the browser button '''
        label = Qt.QLabel("Choose a file (e.g., vtk):")
        self.groupBox_layout.addWidget(label)
        hbox = Qt.QHBoxLayout()
        self.qt_file_name = Qt.QLineEdit()
        hbox.addWidget(self.qt_file_name) 
        self.qt_browser_button = Qt.QPushButton('Browser')
        self.qt_browser_button.clicked.connect(self.on_file_browser_clicked)
        self.qt_browser_button.show()
        hbox.addWidget(self.qt_browser_button)
        file_widget = Qt.QWidget()
        file_widget.setLayout(hbox)
        self.groupBox_layout.addWidget(file_widget)
 
        ''' Add the Open button '''
        self.open_press = 0
        self.qt_open_button = Qt.QPushButton('Open')
        self.qt_open_button.clicked.connect(self.open_vtk_file)
        self.qt_open_button.show()
        self.groupBox_layout.addWidget(self.qt_open_button)
      
        ''' Add the widgets for arrow plot '''
        hbox_arrowplot = Qt.QHBoxLayout()
        self.qt_arrow_checkbox = Qt.QCheckBox("Arrow Plot ")
        self.qt_arrow_checkbox.setChecked(False)
        self.qt_arrow_checkbox.toggled.connect(self.on_arrow_checkbox_change)  
        hbox_arrowplot.addWidget(self.qt_arrow_checkbox) 
        arrowscaleLabel = Qt.QLabel("    Choose arrow scale:")
        hbox_arrowplot.addWidget(arrowscaleLabel)
        self.arrow_scale = Qt.QDoubleSpinBox()
         # set the initial values of some parameters
        self.arrow_scale.setValue(0.03)
        self.arrow_scale.setRange(0, 1)
        self.arrow_scale.setSingleStep (0.01)
        hbox_arrowplot.addWidget(self.arrow_scale)
        arrow_widget = Qt.QWidget()
        arrow_widget.setLayout(hbox_arrowplot)
        self.groupBox_layout.addWidget(arrow_widget)


        vbox_streamline = Qt.QVBoxLayout()
        hbox_streamline = Qt.QHBoxLayout()
        self.qt_streamline_checkbox = Qt.QCheckBox("Streamline ")
        self.qt_streamline_checkbox.setChecked(False)
        self.qt_streamline_checkbox.toggled.connect(self.on_streamline_checkbox_change)
        hbox_streamline.addWidget(self.qt_streamline_checkbox) 
        seedLabel = Qt.QLabel("    Set number of seeds:")
        hbox_streamline.addWidget(seedLabel)
        self.number_seeds = Qt.QDoubleSpinBox()
         # set the initial values of some parameters
        self.number_seeds.setValue(10)
        self.number_seeds.setRange(1, 2000)
        self.number_seeds.setSingleStep (1)
        hbox_streamline.addWidget(self.number_seeds)
        streamline_hwidget = Qt.QWidget()
        streamline_hwidget.setLayout(hbox_streamline)
        #self.groupBox_layout.addWidget(streamline_widget)
        vbox_streamline.addWidget(streamline_hwidget)
     
        vbox_seed_strategy = Qt.QVBoxLayout()
        seedinglabel = Qt.QLabel("Select Seeding Strategy: ")
        vbox_seed_strategy.addWidget(seedinglabel)
        # Add radio buttons for the selection of the seed generation strategy
        self.uniform_seed_radio = Qt.QRadioButton("Uniform Seeding")
        self.uniform_seed_radio.setChecked(True)
        self.uniform_seed_radio.toggled.connect(self.on_seeding_strategy)
        vbox_seed_strategy.addWidget(self.uniform_seed_radio)

        self.random_seed_radio = Qt.QRadioButton("Random Seeding")
        self.random_seed_radio.setChecked(False)
        self.random_seed_radio.toggled.connect(self.on_seeding_strategy)
        vbox_seed_strategy.addWidget(self.random_seed_radio)

        self.seed_widget_radio = Qt.QRadioButton("Seeding Line Widget")
        self.seed_widget_radio.setChecked(False)
        self.seed_widget_radio.toggled.connect(self.on_seeding_strategy)
        vbox_seed_strategy.addWidget(self.seed_widget_radio)
        self.seeding_strategy = 0 # Uniform seeding is the default strategy 


        vbox_render_style = Qt.QVBoxLayout()
        renderlabel = Qt.QLabel("Select Presentation ")
        vbox_render_style.addWidget(renderlabel)
        # Add radio buttons for the selection of stream presentation
        self.line_radio = Qt.QRadioButton("Line Presentation")
        self.line_radio.setChecked(True)
        self.line_radio.toggled.connect(self.on_rendering_style)
        vbox_render_style.addWidget(self.line_radio)

        self.tube_radio = Qt.QRadioButton("Tube Presentation")
        self.tube_radio.setChecked(False)
        self.tube_radio.toggled.connect(self.on_rendering_style)
        vbox_render_style.addWidget(self.tube_radio)

        self.ribbon_radio = Qt.QRadioButton("Ribbon Presentation")
        self.ribbon_radio.setChecked(False)
        self.ribbon_radio.toggled.connect(self.on_rendering_style)
        vbox_render_style.addWidget(self.ribbon_radio)
        self.rendering_style = 1 # line presentation is the default rendering style

        seedingstrategy = Qt.QWidget()
        seedingstrategy.setLayout(vbox_seed_strategy)
        vbox_streamline.addWidget(seedingstrategy)

        renderingstyle = Qt.QWidget()
        renderingstyle.setLayout(vbox_render_style)
        vbox_streamline.addWidget(renderingstyle)


        streamline_widgets = Qt.QWidget()
        streamline_widgets.setLayout(vbox_streamline)
        self.groupBox_layout.addWidget(streamline_widgets)

        ''' Add widgets for Bonus: vtkRuledSurfaceFilter '''
        hbox_surface = Qt.QHBoxLayout()
        self.rf_checkbox = Qt.QCheckBox("vtkRuledSurface On ")
        self.rf_checkbox.setChecked(False)
        self.rf_checkbox.toggled.connect(self.on_ruledSurface_checkbox_change)  
        hbox_surface.addWidget(self.rf_checkbox) 
        seedLabel = Qt.QLabel("    Choose seed number:")
        hbox_surface.addWidget(seedLabel)
        self.seed_number = Qt.QDoubleSpinBox()
         # set the initial values of some parameters
        self.seed_number.setValue(10)
        self.seed_number.setRange(1, 2000)
        self.seed_number.setSingleStep (1)
        hbox_surface.addWidget(self.seed_number)
        surface_widget = Qt.QWidget()
        surface_widget.setLayout(hbox_surface)
        self.groupBox_layout.addWidget(surface_widget)


        self.linewidget_on = 0
        self.st_act = 0
        self.s_act = 0



        
    def on_file_browser_clicked(self):
        dlg = Qt.QFileDialog()
        dlg.setFileMode(Qt.QFileDialog.AnyFile)
        dlg.setNameFilter("loadable files (*.vtk *.mhd)")
        
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.qt_file_name.setText(filenames[0])
    
    def open_vtk_file(self):
        '''Read and verify the vtk input file '''
        input_file_name = self.qt_file_name.text()
        
        if ".mhd" in input_file_name: #The input file is MetaImageData
            self.input_type = "mhd"
            self.reader = vtk.vtkMetaImageReader()
            self.reader.SetFileName(input_file_name)
            self.reader.Update()
        elif ".vtk" in input_file_name: # The input file is VTK
            self.input_type = "vtk"
            self.reader = vtk.vtkDataSetReader()
            self.reader.SetFileName(input_file_name)
            self.reader.Update()       
        
        # Some initialization to remove actors that are created previously
            
        if hasattr(self, 'outline'):
            self.ren.RemoveActor(self.outline)
        
        # You need to modify the following actors' names based on how you define them!!!!!
        if hasattr(self, 'arrow_actor'):
            self.ren.RemoveActor(self.arrow_actor)
        
        if hasattr(self, 'streamline_actor'):
            self.ren.RemoveActor(self.streamline_actor)
            
        if hasattr(self, 'lic_actor'):
            self.ren.RemoveActor(self.lic_actor) 

        self.seeding_strategy = 0 # Uniform seeding is the default strategy

        # Get the data outline
        outlineData = vtk.vtkOutlineFilter()
        outlineData.SetInputConnection(self.reader.GetOutputPort())
        outlineData.Update()

        mapOutline = vtk.vtkPolyDataMapper()
        mapOutline.SetInputConnection(outlineData.GetOutputPort())

        self.outline = vtk.vtkActor()
        self.outline.SetMapper(mapOutline)
        colors = vtk.vtkNamedColors()
        self.outline.GetProperty().SetColor(colors.GetColor3d("Black"))
        self.outline.GetProperty().SetLineWidth(2.)
        
        self.ren.AddActor(self.outline)
        self.ren.ResetCamera()
        self.vtkWidget.GetRenderWindow().Render()   

        self.open_press = 1
        
        
        

    
    ''' Use the vtkGlyph2D filter to show an arrow plot on a 2D surface'''
    def on_arrow_checkbox_change(self):
        if self.qt_arrow_checkbox.isChecked() == True:
            
            # Make sure we use the velocity field
            self.reader.GetOutput().GetPointData().SetActiveVectors("velocity")
            self.reader.GetOutput().GetPointData().SetActiveScalars("magnitude")

            '''Complete the arrow plot visualization here '''


             #to avoid density of the arrows
            densityFilter = vtk.vtkMaskPoints()
            densityFilter.SetInputData(self.reader.GetOutput())
            densityFilter.RandomModeOn() # enable the random sampling mechanism
            #densityFilter.SetRandomModeType() #specify the sampling mode
            densityFilter.SetMaximumNumberOfPoints(2000)
            densityFilter.Update()
            #bonus

           
            #First, Choose the arrow 
            arrow = vtk.vtkArrowSource()
            arrow.Update()

            #Second, setup a vtkGlyph2D object.
            glyph3D = vtk.vtkGlyph3D()
            glyph3D.SetSourceConnection(arrow.GetOutputPort())
            #glyph2D.SetInputData(self.reader.GetOutput())
            glyph3D.SetInputData(densityFilter.GetOutput()) #bonus
            glyph3D.OrientOn()
            glyph3D.SetScaleModeToScaleByVector()
            glyph3D.SetScaleFactor(0.1) # adjust the length of the arrows accordingly
            glyph3D.SetVectorModeToUseVector()
            glyph3D.SetColorModeToColorByScalar()
            glyph3D.Update()
            #Third, create a mapper and add an actor to show the arrows.

            arrows_mapper = vtk.vtkPolyDataMapper()
            arrows_mapper.SetInputConnection(glyph3D.GetOutputPort())
            arrows_mapper.ScalarVisibilityOff()
            arrows_mapper.Update()
            self.arrow_actor = vtk.vtkActor()
            self.arrow_actor.SetMapper(arrows_mapper)
            self.arrow_actor.GetProperty().SetColor(0,1,0.5) # set the color you want

            #add arrow_actor to rendering
            self.ren.AddActor(self.arrow_actor)
            self.ren.ResetCamera()
            
        # Turn on the following if you want to disable the arrow plots
        # But again you need to modify the "arrow_actor" name based on what you use!!!
        else:
            self.ren.RemoveActor(self.arrow_actor)
            
        # Re-render the screen
        self.vtkWidget.GetRenderWindow().Render()
        
    '''even handle for the radio buttons of seeding strategies
    '''
    def on_seeding_strategy(self):
        if self.uniform_seed_radio.isChecked() == True:
            self.random_seed_radio.setChecked(False)
            self.seed_widget_radio.setChecked(False)
            self.seeding_strategy = 0
        elif self.random_seed_radio.isChecked() ==  True:
            self.uniform_seed_radio.setChecked(False)
            self.seed_widget_radio.setChecked(False)
            self.seeding_strategy = 1
        elif self.seed_widget_radio.isChecked()== True:
            self.random_seed_radio.setChecked(False)
            self.uniform_seed_radio.setChecked(False)
            self.seeding_strategy = 2


    def on_rendering_style(self):
        if self.line_radio.isChecked() == True:
            self.tube_radio.setChecked(False)
            self.ribbon_radio.setChecked(False)
            self.rendering_style = 1
        elif self.tube_radio.isChecked() ==  True:
            self.line_radio.setChecked(False)
            self.ribbon_radio.setChecked(False)
            self.rendering_style = 2
        elif self.ribbon_radio.isChecked()== True:
            self.line_radio.setChecked(False)
            self.tube_radio.setChecked(False)
            self.rendering_style = 3
   
    '''         
        Complete the following function for genenerate uniform seeds 
        for streamline placement

    '''
    def uniform_generate_seeds(self):
        num_seeds = int (self.number_seeds.value())
        seedPoints = vtk.vtkPoints()

        # Generate the uniformly positioned seeds below!!
        nx = int( float(num_seeds)**(1.0/2)) # take the squared root of num_seeds
        bound=self.reader.GetOutput().GetBounds()
        for i in range(0, nx):
            for j in range(0, nx):
                for k in range(0, nx):
                    x = i*1.0/(nx -1)
                    y = j*1.0/(nx -1)
                    z = k*1.0/(nx -1)
                    x_bound=bound[0] + x*(bound[1]-bound[0])
                    y_bound=bound[2] + y*(bound[3]-bound[2])
                    z_bound=bound[4] + z*(bound[5]-bound[4])
                    seedPoints.InsertNextPoint(x_bound, y_bound, z_bound)

        # Need to put the seed points in a vtkPolyData object
        seedPolyData  = vtk.vtkPolyData()
        seedPolyData.SetPoints(seedPoints)
        return seedPolyData


    '''  
        Complete the following function for genenerate random seeds 
        for streamline placement
    '''
    def random_generate_seeds(self):
        numb_seeds = int (self.number_seeds.value())
        seedPoints = vtk.vtkPoints()       

        # Generate the random seeds below!!

        bound=self.reader.GetOutput().GetBounds()
        for i in range(0, numb_seeds):
            x = (random.randint(0,32768)) / 32768.0
            y = (random.randint(0,32768)) / 32768.0
            z = (random.randint(0,32768)) / 32768.0
            x_bound=bound[0] + x*(bound[1]-bound[0])
            y_bound=bound[2] + y*(bound[3]-bound[2])
            z_bound=bound[4] + z*(bound[5]-bound[4])
            seedPoints.InsertNextPoint(x_bound, y_bound, z_bound)

        # Need to put the seed points in a vtkPolyData object
        seedPolyData  = vtk.vtkPolyData()
        seedPolyData.SetPoints(seedPoints)
        return seedPolyData

    def seed_linewidget(self):
        numb_seeds = int(self.number_seeds.value())
        seedPolyData  = vtk.vtkPolyData()
        bound=self.reader.GetOutput().GetBounds()
        #generate linewidget
        self.lineWidget = vtk.vtkLineWidget()
        self.lineWidget.SetResolution(numb_seeds)
        self.lineWidget.SetInputData(self.reader.GetOutput())
        self.lineWidget.GetPolyData(seedPolyData)
        self.lineWidget.SetAlignToYAxis()
        self.lineWidget.ClampToBoundsOn()
        self.lineWidget.PlaceWidget()
        self.seeds1 = seedPolyData
        return seedPolyData

    def BeginInteraction(self, obj, event):
        self.streamline_actor.VisibilityOn()

    def computeStreamline(self, seeds):
        bounds=self.reader.GetOutput().GetBounds()
        xrangeCal = (bounds[1]-bounds[0])
        yrangeCal = (bounds[3]-bounds[2])
        zrangeCal = (bounds[5]-bounds[4])
        diameterDomain = math.sqrt(xrangeCal**2 + yrangeCal**2+zrangeCal**2)
        maxPropagation = 0.8*diameterDomain
        #integStep = (bounds[1]-bounds[0])/256

        # Step 2: Create a vtkStreamTracer object, set input data and seeding points
        stream_tracer = vtk.vtkStreamTracer()
        stream_tracer.SetInputData(self.reader.GetOutput()) # set vector field
        stream_tracer.SetSourceData(seeds) # pass in the seeds
    

        # Step 3: Set the parameters. 
        # Check the reference https://vtk.org/doc/nightly/html/classvtkStreamTracer.html
            # to have the full list of 
        rk4 = vtk.vtkRungeKutta4()
        stream_tracer.SetMaximumPropagation(maxPropagation)
        stream_tracer.SetInitialIntegrationStep(0.1)#integStep)
        stream_tracer.SetIntegratorTypeToRungeKutta45()
        stream_tracer.SetIntegrationDirectionToBoth()
        #stream_tracer.SetComputeVorticity(1)
        stream_tracer.SetIntegrator(rk4)
        # Step 4: choose rendering style
        if self.rendering_style == 1: #line
            stream_mapper = vtk.vtkPolyDataMapper()
            stream_mapper.SetInputConnection(stream_tracer.GetOutputPort())
            stream_mapper.Update()

        elif self.rendering_style == 2: #tube
             # create stream tube
            streamTube = vtk.vtkTubeFilter()
            streamTube.SetInputConnection(stream_tracer.GetOutputPort())
            streamTube.SetInputArrayToProcess(1, 0, 0, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, "vectors")
            streamTube.SetRadius(0.02)
            streamTube.SetNumberOfSides(12)
            streamTube.SetVaryRadiusToVaryRadiusByVector()
            # Visualization
            stream_mapper = vtk.vtkPolyDataMapper()
            stream_mapper.SetInputConnection(streamTube.GetOutputPort())
            #stream_mapper.SetScalarRange(self.reader.GetOutput().GetScalarRange())
            stream_mapper.Update()

        elif self.rendering_style == 3: # ribbon
            streamRibbon = vtk.vtkRibbonFilter()
            streamRibbon.SetInputConnection(stream_tracer.GetOutputPort())
            streamRibbon.SetWidth(0.1)
            streamRibbon.SetGenerateTCoordsToUseLength()
            #streamRibbon.SetTextureLength(1.0)
            streamRibbon.SetAngle(0)
            streamRibbon.UseDefaultNormalOn()
            streamRibbon.SetDefaultNormal(0, 0, 1)
            streamRibbon.SetVaryWidth(0)
                # Visualization
            stream_mapper = vtk.vtkPolyDataMapper()
            stream_mapper.SetInputConnection(streamRibbon.GetOutputPort())
                #stream_mapper.SetScalarRange(self.reader.GetOutput().GetScalarRange())
            stream_mapper.Update()
        return stream_mapper


    def GenerateStreamlines(self, obj, event):
        self.lineWidget.GetPolyData(self.seeds1)
        stream_mapper = self.computeStreamline(self.seeds1)
        self.streamline_actor.SetMapper(stream_mapper)
        self.streamline_actor.GetProperty().SetColor(1,0.2,0) # set the color you want
        if self.st_act== 1:
            self.ren.RemoveActor(self.streamline_actor)
            self.st_act = 0
        self.ren.AddActor(self.streamline_actor)
        self.st_act = 1
        self.ren.ResetCamera()
        self.vtkWidget.GetRenderWindow().Render() 



        
    ''' 
        Complete the following function to generate a set of streamlines
        from the above generated uniform or random seeds
    '''
    def on_streamline_checkbox_change(self):
        if self.open_press == 0:
            return

        if self.qt_streamline_checkbox.isChecked() == True:
           #self.reader.GetOutput().GetPointData().SetActiveVectors("velocity")
            #self.reader.GetOutput().GetPointData().SetActiveScalars("magnitude")
            # Step 1: Create seeding points 
            self.streamline_actor = vtk.vtkActor()
            if self.seeding_strategy == 1: 
                seedPolyData = self.random_generate_seeds() # You also can try generate_seeding_line()
            elif self.seeding_strategy == 0:
                seedPolyData = self.uniform_generate_seeds()
            elif self.seeding_strategy == 2:
                seedPolyData = self.seed_linewidget()
                self.linewidget_on = 1
                # Associate the line widget with the interactor and setup callbacks.

                     
            if self.seeding_strategy == 2:
                self.lineWidget.SetInteractor(self.iren)
                self.lineWidget.AddObserver("StartInteractionEvent", self.BeginInteraction)
                self.lineWidget.AddObserver("InteractionEvent", self.GenerateStreamlines)
            
            # call out computing function
            stream_mapper = self.computeStreamline(seedPolyData)

                  
            self.streamline_actor.SetMapper(stream_mapper)
            
            self.streamline_actor.GetProperty().SetColor(1,0.2,0) # set the color you want
            self.ren.AddActor(self.streamline_actor)
            self.st_act = 1
            if self.seeding_strategy == 2:
                self.lineWidget.EnabledOn()
                self.streamline_actor.VisibilityOn()
                self.lineWidget.GetPolyData(seedPolyData)
                #self.vtkWidget.GetRenderWindow().Render()
            self.ren.ResetCamera()            
        # Turn on the following if you want to disable the streamline visualization
        # But again you need to modify the "streamline_actor" name based on what you use!!!
        else:
            self.ren.RemoveActor(self.streamline_actor)
     
           
        # Re-render the screen
        self.vtkWidget.GetRenderWindow().Render() 
    



    '''BONUS'''
         
    def on_ruledSurface_checkbox_change(self):
        if self.open_press == 0:
            return
        if self.rf_checkbox.isChecked() == True:
            numb_seeds = int(self.seed_number.value())
            self.seeds  = vtk.vtkPolyData()
            bound=self.reader.GetOutput().GetBounds()
            #generate linewidget
            self.line_widget = vtk.vtkLineWidget()
            self.line_widget.SetResolution(numb_seeds)
            self.line_widget.SetInputData(self.reader.GetOutput())
            self.line_widget.GetPolyData(self.seeds)
            self.line_widget.SetAlignToYAxis()
            self.line_widget.ClampToBoundsOn()
            self.line_widget.PlaceWidget()
            print("y1")
            self.surface_actor = vtk.vtkActor()

            surface_mapper = self.computeSurface(self.seeds)
            self.line_widget.SetInteractor(self.iren)
            self.line_widget.AddObserver("StartInteractionEvent", self.BeginInteractionS)
            self.line_widget.AddObserver("InteractionEvent", self.GenerateStreamlinesS)
            self.surface_actor.SetMapper(surface_mapper)
            
            self.surface_actor.GetProperty().SetColor(1.0,0.5,0.5) # set the color you want
            self.ren.AddActor(self.surface_actor)
            self.s_act = 1
            self.line_widget.EnabledOn()
            self.surface_actor.VisibilityOn()
            self.line_widget.GetPolyData(self.seeds)
  
            self.ren.ResetCamera()  

        else:
            self.ren.RemoveActor(self.surface_actor)
            self.s_act = 0
     
        # Re-render the screen
        self.vtkWidget.GetRenderWindow().Render() 

    def BeginInteractionS(self, obj, event):
        self.surface_actor.VisibilityOn()

    def GenerateStreamlinesS(self, obj, event):
        self.line_widget.GetPolyData(self.seeds)
        surface_mapper = self.computeSurface(self.seeds)
        self.surface_actor.SetMapper(surface_mapper)
        self.surface_actor.GetProperty().SetColor(1,0.5,0.5) # set the color you want
        if self.s_act == 1:
            self.ren.RemoveActor(self.surface_actor)
            self.s_act = 0
        self.ren.AddActor(self.surface_actor)
        self.s_act = 1
        self.ren.ResetCamera()
        self.vtkWidget.GetRenderWindow().Render() 

    def computeSurface(self, seeds):
        bounds=self.reader.GetOutput().GetBounds()
        xrangeCal = (bounds[1]-bounds[0])
        yrangeCal = (bounds[3]-bounds[2])
        zrangeCal = (bounds[5]-bounds[4])
        diameterDomain = math.sqrt(xrangeCal**2 + yrangeCal**2+zrangeCal**2)
        maxPropagation = 0.5*diameterDomain
        integStep = (bounds[1]-bounds[0])/256

        # Step 2: Create a vtkStreamTracer object, set input data and seeding points
        surface_tracer = vtk.vtkStreamTracer()
        surface_tracer.SetInputData(self.reader.GetOutput()) # set vector field
        surface_tracer.SetSourceData(seeds) # pass in the seeds
        rk4 = vtk.vtkRungeKutta4()
        surface_tracer.SetMaximumPropagation(maxPropagation)
            #stream_tracer.SetInitialIntegrationStep(integStep)
        surface_tracer.SetIntegratorTypeToRungeKutta45()
        surface_tracer.SetIntegrationDirectionToBoth()
            #stream_tracer.SetComputeVorticity(1)
        surface_tracer.SetIntegrator(rk4)   
        surfaceFilter = vtk.vtkRuledSurfaceFilter()
        surfaceFilter.SetInputConnection(surface_tracer.GetOutputPort())
        surfaceFilter.SetOffset(0)
        surfaceFilter.SetOnRatio(2) 
        surfaceFilter.PassLinesOn()
        surfaceFilter.SetRuledModeToPointWalk()
        surfaceFilter.SetDistanceFactor(30)
        surface_mapper = vtk.vtkPolyDataMapper()
        surface_mapper.SetInputConnection(surfaceFilter.GetOutputPort())
        surface_mapper.Update()

        return surface_mapper

   
        
if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())