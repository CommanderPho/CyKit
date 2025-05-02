import numpy as np
import pyvista as pv
import time
import sys
import queue
from pathlib import Path

# Add CyKit paths
# sys.path.insert(0, '..//py3//cyUSB//')
# sys.path.insert(0, '..//py3')

# Create a queue for EEG data
tasks = queue.Queue()

# Electrode names (adjust based on your headset)
electrode_names = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

class EEGVisualizer:
    def __init__(self):
        # Initialize EEG connection similar to example_epoc_plus.py
        self.eeg = EEG()
        
        # Set up PyVista visualization
        self.plotter = pv.Plotter()
        
        # Load the 3D model (use your model path)
        model_path = Path('EXTERNAL\meshes\CompleteEmotivEpocEEG.glb').resolve()
        assert model_path.exists()
        self.headset = pv.read(model_path)  # or .obj
        
        # Get electrode submeshes by name
        self.electrodes = {}
        for name in electrode_names:
            # Assuming your submeshes are named appropriately
            self.electrodes[name] = self.headset.get_block_by_name(name)
            
        # Set initial colors (all yellow - neutral)
        self.update_electrode_colors([1] * len(electrode_names))
        
        # Add model to the scene
        self.plotter.add_mesh(self.headset)
        
    def update_electrode_colors(self, quality_values):
        """
        Update electrode colors based on quality values
        quality_values: list of values between 0 and 1 (0=bad, 1=good)
        """
        for i, name in enumerate(electrode_names):
            # Create color: red (bad) to green (good)
            quality = quality_values[i]
            color = [1-quality, quality, 0]  # R,G,B
            
            # Update electrode color
            self.electrodes[name].color = color
            
        # Update the render
        self.plotter.update()
    
    def run(self):
        # Start the visualization
        self.plotter.show(interactive=False)
        
        while True:
            # Get data from EEG
            if not tasks.empty():
                data = self.eeg.get_data()
                
                # Process data to get electrode quality (example)
                # This would depend on how your headset reports quality
                quality_values = self.process_quality(data)
                
                # Update visualization
                self.update_electrode_colors(quality_values)
                
            # Update the render
            self.plotter.update()
            time.sleep(0.1)
    
    def process_quality(self, data):
        """
        Process EEG data to determine electrode quality
        This is a placeholder - you'll need to implement based on your headset
        """
        # Example: parse data string into values
        values = [float(x) for x in data.split(', ')]
        
        # Convert values to quality indicators (0-1)
        # This is just an example - you'll need to implement your own logic
        quality_values = []
        for value in values[:len(electrode_names)]:
            # Example threshold-based quality (adjust based on your data)
            if 4200 <= value <= 4300:  # Good range
                quality = 1.0
            else:
                # Calculate distance from good range
                distance = min(abs(value - 4200), abs(value - 4300))
                quality = max(0, 1 - (distance / 100))
            
            quality_values.append(quality)
            
        return quality_values

# Run the visualizer
if __name__ == "__main__":
    visualizer = EEGVisualizer()
    visualizer.run()
