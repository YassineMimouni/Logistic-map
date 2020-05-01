import plotly
import plotly.graph_objects as go
import warnings 
from Mandelbrot3D import Mand_3D

warnings.filterwarnings("ignore")


def animation(mand):

        """ Animate the rotation of the Mandelbrot set in 3D.  
            Show the link between Mandelbrot set and bifurcation diagram.  
            
            :return: Rotation of the Mandelbrot set in 3D   
            :rtype: Animation 3D"""

        anim = mand.interact() 

        updatemenus=[dict(type='buttons',
                  showactive=False,
                  y=1,
                  x=0.8,
                  xanchor='left',
                  yanchor='bottom',
                  pad=dict(t=45, r=10),
                  buttons=[dict(label='Play',
                                 method='animate',
                                 args=[None, dict(frame=dict(duration=0, redraw=True), 
                                                             transition=dict(duration=0),
                                                             fromcurrent=True,
                                                             mode='immediate'
                                                            )])])]

        anim.update_layout(updatemenus=updatemenus, title = 'Mandelbrot 3D animation')


        frames = []

        xt = 0
        yt = -0.8
        zt = 2.5

        for t in range(20):
            xt = xt
            yt = yt - 0.0375
            zt = zt - 0.0550
            frames.append(go.Frame(layout=dict(scene_camera_eye=dict(x=xt,y=yt,z=zt))))
    
        anim.frames=frames

        return anim