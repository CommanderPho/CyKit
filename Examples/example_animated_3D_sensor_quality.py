import numpy as np
import pyvista as pv
import time
import sys
import random
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
    def __init__(self, model_path=None, update_interval=0.5):
        """
        Initialize the EEG visualizer
        
        Parameters:
        -----------
        model_path : str or Path, optional
            Path to the 3D model file (.glb or .obj)
        update_interval : float, optional
            Time interval between updates in seconds (default: 0.5)
        """
        self.update_interval = update_interval
        
        # Set up PyVista visualization
        self.plotter = pv.Plotter()
        
        # Load the 3D model
        if model_path is None:
            model_path = Path('EXTERNAL/meshes/CompleteEmotivEpocEEG.glb').resolve()
        else:
            model_path = Path(model_path).resolve()
            
        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found: {model_path}")
            
        print(f"Loading 3D model from: {model_path}")
        self.headset = pv.read(model_path)
        
        # Get electrode submeshes by name
        self.electrodes = {}
        for name in electrode_names:
            try:
                # Try to get block by name
                self.electrodes[name] = self.headset.get_block_by_name(name)
                print(f"Found electrode: {name}")
            except Exception as e:
                print(f"Warning: Could not find electrode '{name}' in the model: {e}")
                # If we can't find the electrode, we'll create a placeholder
                # This is just so the script doesn't crash if the model doesn't have all electrodes
                sphere = pv.Sphere(radius=0.01, center=(0, 0, 0))
                sphere.name = name
                self.electrodes[name] = sphere
        
        # Set initial colors (all yellow - neutral)
        self.update_electrode_colors([0.5] * len(electrode_names))
        
        # Add model to the scene
        self.plotter.add_mesh(self.headset)
        
        # Add a title
        self.plotter.add_text("EEG Electrode Quality Visualization\nRed = Poor Quality, Green = Good Quality", 
                              position="upper_left", font_size=12, color='white')
        
    def update_electrode_colors(self, quality_values):
        """
        Update electrode colors based on quality values
        
        Parameters:
        -----------
        quality_values: list of values between 0 and 1 (0=bad, 1=good)
        """
        for i, name in enumerate(electrode_names):
            if i < len(quality_values) and name in self.electrodes:
                # Create color: red (bad) to green (good)
                quality = quality_values[i]
                color = [1-quality, quality, 0]  # R,G,B
                
                # Update electrode color
                self.electrodes[name].color = color
        
        # Update the render
        self.plotter.update()
    
    def generate_random_quality(self):
        """Generate random quality values for testing"""
        return [random.uniform(0, 1) for _ in range(len(electrode_names))]
    
    def run(self):
        """Run the visualization with random data updates"""
        # Start the visualization
        self.plotter.show(interactive=False, auto_close=False)
        
        print("Starting visualization with random quality values...")
        print("Press Ctrl+C to exit")
        
        try:
            while True:
                # Generate random quality values
                quality_values = self.generate_random_quality()
                
                # Update visualization
                self.update_electrode_colors(quality_values)
                
                # Print current values for debugging
                quality_str = ", ".join([f"{name}: {quality:.2f}" for name, quality in zip(electrode_names, quality_values)])
                print(f"Quality values: {quality_str}")
                
                # Wait for next update
                time.sleep(self.update_interval)
                
        except KeyboardInterrupt:
            print("Visualization stopped by user")
        finally:
            # Close the plotter
            self.plotter.close()

# Run the visualizer
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='EEG Electrode Quality Visualizer')
    parser.add_argument('--model', type=str, help='Path to the 3D model file (.glb or .obj)')
    parser.add_argument('--interval', type=float, default=0.5, help='Update interval in seconds (default: 0.5)')
    
    args = parser.parse_args()
    
    try:
        visualizer = EEGVisualizer(model_path=args.model, update_interval=args.interval)
        visualizer.run()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
