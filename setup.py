#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Scott E. Townsend',
 'author_email': 'scott.e.townsend@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'Component wrapper for VSP (Vehicle Sketch Pad)',
 'download_url': '',
 'entry_points': '[openmdao.parametric_geometry]\nvsp_wrapper.parageom.VSPParametricGeometry=vsp_wrapper.parageom:VSPParametricGeometry\n\n[openmdao.component]\nvsp_wrapper.wrapper.VSP=vsp_wrapper.wrapper:VSP\n\n[openmdao.container]\nvsp_wrapper.component.VSPComponent=vsp_wrapper.component:VSPComponent\nvsp_wrapper.blank.BlankParms=vsp_wrapper.blank:BlankParms\nvsp_wrapper.cabin.CrossSection=vsp_wrapper.cabin:CrossSection\nvsp_wrapper.external.ExternalParms=vsp_wrapper.external:ExternalParms\nvsp_wrapper.havoc.HavocParms=vsp_wrapper.havoc:HavocParms\nvsp_wrapper.source.LineSource=vsp_wrapper.source:LineSource\nvsp_wrapper.user.UserParms=vsp_wrapper.user:UserParms\nvsp_wrapper.pod.PodParms=vsp_wrapper.pod:PodParms\nvsp_wrapper.user.User=vsp_wrapper.user:User\nvsp_wrapper.general.GeneralParms=vsp_wrapper.general:GeneralParms\nvsp_wrapper.wing_sect.WingSect=vsp_wrapper.wing_sect:WingSect\nvsp_wrapper.fuselage.OMLParms=vsp_wrapper.fuselage:OMLParms\nvsp_wrapper.engine.Engine=vsp_wrapper.engine:Engine\nvsp_wrapper.source.BaseSource=vsp_wrapper.source:BaseSource\nvsp_wrapper.wrapper.VSP=vsp_wrapper.wrapper:VSP\nvsp_wrapper.fuselage.MLParms=vsp_wrapper.fuselage:MLParms\nvsp_wrapper.prop.PropParms=vsp_wrapper.prop:PropParms\nvsp_wrapper.blank.Blank=vsp_wrapper.blank:Blank\nvsp_wrapper.havoc.Havoc=vsp_wrapper.havoc:Havoc\nvsp_wrapper.fuselage2.CrossSection=vsp_wrapper.fuselage2:CrossSection\nvsp_wrapper.fuselage2.Fuselage2=vsp_wrapper.fuselage2:Fuselage2\nvsp_wrapper.airfoil.Airfoil=vsp_wrapper.airfoil:Airfoil\nvsp_wrapper.prop.SectParms=vsp_wrapper.prop:SectParms\nvsp_wrapper.fuselage2.FuseParms=vsp_wrapper.fuselage2:FuseParms\nvsp_wrapper.fuselage.CrossSection=vsp_wrapper.fuselage:CrossSection\nvsp_wrapper.duct.DuctParms=vsp_wrapper.duct:DuctParms\nvsp_wrapper.fuselage.IMLParms=vsp_wrapper.fuselage:IMLParms\nvsp_wrapper.cabin.CabinLayoutParms=vsp_wrapper.cabin:CabinLayoutParms\nvsp_wrapper.mesh.MeshParms=vsp_wrapper.mesh:MeshParms\nvsp_wrapper.pod.Pod=vsp_wrapper.pod:Pod\nvsp_wrapper.fuselage.FuseParms=vsp_wrapper.fuselage:FuseParms\nvsp_wrapper.geometry.VSPGeometry=vsp_wrapper.geometry:VSPGeometry\nvsp_wrapper.prop.Prop=vsp_wrapper.prop:Prop\nvsp_wrapper.ms_wing.MSWingParms=vsp_wrapper.ms_wing:MSWingParms\nvsp_wrapper.hwb.HWBParms=vsp_wrapper.hwb:HWBParms\nvsp_wrapper.external.External=vsp_wrapper.external:External\nvsp_wrapper.source.PointSource=vsp_wrapper.source:PointSource\nvsp_wrapper.cabin.CabinLayout=vsp_wrapper.cabin:CabinLayout\nvsp_wrapper.xml_container.XMLContainer=vsp_wrapper.xml_container:XMLContainer\nvsp_wrapper.wing.WingParms=vsp_wrapper.wing:WingParms\nvsp_wrapper.ms_wing.MSWing=vsp_wrapper.ms_wing:MSWing\nvsp_wrapper.engine.EngineParms=vsp_wrapper.engine:EngineParms\nvsp_wrapper.wing.Wing=vsp_wrapper.wing:Wing\nvsp_wrapper.hwb.HWB=vsp_wrapper.hwb:HWB\nvsp_wrapper.duct.Duct=vsp_wrapper.duct:Duct\nvsp_wrapper.window.VirtWindow=vsp_wrapper.window:VirtWindow\nvsp_wrapper.texture.Texture=vsp_wrapper.texture:Texture\nvsp_wrapper.mesh.Mesh=vsp_wrapper.mesh:Mesh\nvsp_wrapper.fuselage.Fuselage=vsp_wrapper.fuselage:Fuselage\nvsp_wrapper.source.BoxSource=vsp_wrapper.source:BoxSource',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Scott E. Townsend',
 'maintainer_email': 'scott.e.townsend@nasa.gov',
 'name': 'vsp_wrapper',
 'package_data': {'vsp_wrapper': ['sphinx_build/html/index.html',
                                  'sphinx_build/html/.buildinfo',
                                  'sphinx_build/html/py-modindex.html',
                                  'sphinx_build/html/objects.inv',
                                  'sphinx_build/html/searchindex.js',
                                  'sphinx_build/html/search.html',
                                  'sphinx_build/html/pkgdocs.html',
                                  'sphinx_build/html/usage.html',
                                  'sphinx_build/html/genindex.html',
                                  'sphinx_build/html/srcdocs.html',
                                  'sphinx_build/html/_sources/usage.txt',
                                  'sphinx_build/html/_sources/pkgdocs.txt',
                                  'sphinx_build/html/_sources/index.txt',
                                  'sphinx_build/html/_sources/srcdocs.txt',
                                  'sphinx_build/html/_static/plus.png',
                                  'sphinx_build/html/_static/comment-bright.png',
                                  'sphinx_build/html/_static/comment.png',
                                  'sphinx_build/html/_static/down-pressed.png',
                                  'sphinx_build/html/_static/sidebar.js',
                                  'sphinx_build/html/_static/doctools.js',
                                  'sphinx_build/html/_static/ajax-loader.gif',
                                  'sphinx_build/html/_static/default.css',
                                  'sphinx_build/html/_static/down.png',
                                  'sphinx_build/html/_static/jquery.js',
                                  'sphinx_build/html/_static/underscore.js',
                                  'sphinx_build/html/_static/minus.png',
                                  'sphinx_build/html/_static/up-pressed.png',
                                  'sphinx_build/html/_static/up.png',
                                  'sphinx_build/html/_static/pygments.css',
                                  'sphinx_build/html/_static/searchtools.js',
                                  'sphinx_build/html/_static/file.png',
                                  'sphinx_build/html/_static/basic.css',
                                  'sphinx_build/html/_static/websupport.js',
                                  'sphinx_build/html/_static/comment-close.png',
                                  'sphinx_build/html/_modules/index.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/user.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/cabin.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/duct.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/component.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/geometry.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/havoc.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/external.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/texture.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/wing.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/hwb.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/source.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/airfoil.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/fuselage2.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/general.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/blank.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/engine.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/ms_wing.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/fuselage.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/wing_sect.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/mesh.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/prop.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/window.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/pod.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/wrapper.html',
                                  'sphinx_build/html/_modules/vsp_wrapper/xml_container.html',
                                  'test/Schweizer2_32.xml',
                                  'test/test_parageom.py',
                                  'test/Cessna182.xml',
                                  'test/eagle_eye.xml',
                                  'test/777.xml',
                                  'test/Cessna182.vsp',
                                  'test/hwb.xml',
                                  'test/openmdao_log.txt',
                                  'test/GE90.xml',
                                  'test/m6_singleside.xml',
                                  'test/test_wrapper.py']},
 'package_dir': {'': 'src'},
 'packages': ['vsp_wrapper'],
 'url': 'https://github.com/OpenMDAO-Plugins/vsp_wrapper',
 'version': '0.8',
 'zip_safe': False}


setup(**kwargs)

