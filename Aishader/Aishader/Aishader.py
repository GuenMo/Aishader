# -*- coding: utf-8 -*-


import maya.cmds as cmds

import maya.mel as mel 
import arnold 
import mtoa
#ArnoldShader_Library 


class Aishader():
	def __init__(self):

		windowName = 'aishader'

		if cmds.window(windowName,ex=1) :  
			cmds.deleteUI(windowName)
		elif cmds.windowPref(windowName,ex=1) :
			cmds.windowPref(windowName,r=1)

	
		aishader = cmds.window(windowName , title='ArnoldShader',rtf=1,wh=(300,100))

		cmds.rowColumnLayout('Col',nc=2)
		#cmds.columnLayout('Col')

		cmds.frameLayout('frame',l=' D_aishader ',bs='etchedOut',p='Col')
		
		cmds.columnLayout( columnAttach=('both', 10), rowSpacing=20, columnWidth=60 )
		#cmds.gridLayout( nrc = (5,5), cellWidthHeight=(60, 60))
		
		appPath = __file__.replace("\\", "/")
		rootPath = appPath.rpartition("/")[0]
		iconPath = rootPath + '/Icon'

		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/AiStandard.png', label='aiStandard',command = self.aiStandard_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/AiSkin.png', label='aiSkin',command = self.aiSkin_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/AiHair.png', label='aiHair',command = self.aiHair_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/AiAmbientOcclusion.png', label='aiAmbientOcclusion',command = self.aiAmbientOcclusion_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/AiShadowCatcher.png', label='Shadow',command = self.aiShadowCatcher_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/AiMotionVector.png', label='MotionVector',command = self.aiMotionVector_shd_Edit)
		
		cmds.frameLayout('frame1',l=' Edit_ArnoldShader_Library ',bs='etchedIn',p='Col')
		cmds.gridLayout('Col', nrc = (5,5), cellWidthHeight=(60, 60))
		
		
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Balloon.png', label='Balloon',command = self.Balloon_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Car paint.png', label='CarPaint',command = self.CarPaint_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Ceramic.png', label='Ceramic',command = self.Ceramic_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Chocolate.png', label='Chocolate',command = self.Chocolate_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Chrome.png', label='Chrome',command = self.chrome_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Clay.png', label='Clay',command = self.Clay_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Glass.png', label='Glass',command = self.Glass_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Gold.png', label='Gold',command = self.Gold_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Incandescent.png', label='Glow',command = self.Incandescent_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Matt.png', label='Matt',command = self.Matt_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/MattPlastic.png', label='MattPlastic',command = self.MattPlastic_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/MetallicCarPaint.png', label='MetallicCarP',command = self.MetallicCarPaint_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/PlasticToy.png', label='plasticToy',command = self.plasticToy_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/ShinyPlastic.png', label='ShinyPlastic',command = self.ShinyPlastic_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/SilkMattP_A.png', label='SilkMattP_A',command = self.SilkMattP_A_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/SilkMattP_B.png', label='SilkMattP_B',command = self.SilkMattP_B_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/SoftPlastic.png', label='SoftPlastic',command = self.SoftPlastic_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Styrofoam.png', label='Styrofoam',command = self.Styrofoam_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/TableCloth.png', label='TableCloth',command = self.TableCloth_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Velvet.png', label='Velvet',command = self.Velvet_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/WallPlaste.png', label='WallPlaster',command = self.WallPlaster_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Wax.png', label='Wax',command = self.Wax_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/WheelRims.png', label='WheelRims',command = self.WheelRims_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Water.png', label='Water',command = self.Water_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/TransparentPlastic.png', label='TransparentPlastic',command = self.TransparentPlastic_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Bubbl.png', label='Bubbl',command = self.Bubbl_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Wood.png', label='Wood',command = self.Wood_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/FacingRatio.png', label='FacingRatio',command = self.facingRatio_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Rim.png', label='Rim',command = self.Rim_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Wire.png', label='Wire',command = self.Wire_shd_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Toon_Obq.png', label='Toon_Obq',command = self.ObqToon_Edit)
		#cmds.iconTextButton( style='iconAndTextVertical', label='',command =' ')
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Toon_A.png', label='Toon_A',command = self.Toon_A_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Toon_B.png', label='Toon_B',command = self.Toon_B_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Toon_AB.png', label='Toon_AB',command = self.Toon_AB_Edit)
		cmds.iconTextButton( style='iconAndTextVertical',image =iconPath +'/Ocen.png', label='Ocen',command = self.Ocen_Edit)
		
		
		#cmds.iconTextButton( style='iconAndTextVertical',image ='O:/Gale_Tools/Render/ArnoldShader/Icon/icons/R.png', label='R',command = 'R_shd_Edit()')
		#cmds.iconTextButton( style='iconAndTextVertical',image ='O:/Gale_Tools/Render/ArnoldShader/Icon/icons/G.png', label='G',command = 'G_shd_Edit()')
		#cmds.iconTextButton( style='iconAndTextVertical',image ='O:/Gale_Tools/Render/ArnoldShader/Icon/icons/B.png', label='B',command = 'B_shd_Edit()')
		
		cmds.window( aishader ,e=1,rtf=1)
		cmds.showWindow( aishader )
		cmds.window(windowName,e=1,tlc=(190,40) )

	
	#기본aishader
	def aiStandard_shd_Edit(self, *args):
		aiStandard_shd = cmds.shadingNode('aiStandard', n = 'aiStandard' , asShader=True)	
	
	#기본aiSkin
	def aiSkin_shd_Edit(self, *args):
		aiSkin_shd = cmds.shadingNode('aiSkin', n = 'aiSkin' , asShader=True)
	#기본aiSkin #uvcood 자동입력
	def aiHair_shd_Edit(self, *args):
		aiHair_shd = cmds.shadingNode('aiHair', n = 'aiHair' , asShader=True)
		cmds.setAttr(aiHair_shd+'.uparam' , 'uparamcoord' ,type = 'string')
		cmds.setAttr(aiHair_shd+'.vparam' , 'vparamcoord' ,type = 'string')
		cmds.setAttr(aiHair_shd+'.rootcolor', 0.3, 0.12, 0.05, type='double3')
		cmds.setAttr(aiHair_shd+'.tipcolor', 0.6, 0.25, 0.1, type='double3')
		cmds.setAttr(aiHair_shd+'.specColor', 0.9, 0.6, 0.3, type='double3')
		cmds.setAttr(aiHair_shd+'.kdInd', 1)
	#기본aiAmbientOcclusion
	def aiAmbientOcclusion_shd_Edit(self, *args):
		aiAmbientOcclusion_shd = cmds.shadingNode('aiAmbientOcclusion', n = 'aiAmbientOcclusion' , asShader=True)
	#기본그림자
	def aiShadowCatcher_shd_Edit(self, *args):
		aiShadowCatcher_shd = cmds.shadingNode('aiShadowCatcher', n = 'aiShadowCatcher' , asShader=True)
		cmds.setAttr(aiShadowCatcher_shd+'.shadowColor', 0.5, 0.5, 0.5, type='double3')
	#기본모션백터
	def aiMotionVector_shd_Edit(self, *args):
		aiMotionVector_shd = cmds.shadingNode('aiMotionVector', n = 'aiMotionVector' , asShader=True)
		
	#Balloon(풍선쉐이더)
	def Balloon_shd_Edit(self, *args):
		Balloon_shd = cmds.shadingNode('aiStandard', n = 'Balloon' , asShader=True)
		cmds.setAttr(Balloon_shd+'.color', 0.781, 0.927, 1, type='double3')
		cmds.setAttr(Balloon_shd+'.diffuseRoughness', 0.423)
		cmds.setAttr(Balloon_shd+'.Kb', 1)
		cmds.setAttr(Balloon_shd+'.Ks', 0.222)
		cmds.setAttr(Balloon_shd+'.specularRoughness', 0.453)
		cmds.setAttr(Balloon_shd+'.specularFresnel', 1)
		cmds.setAttr(Balloon_shd+'.Ksn',  0.556)
		cmds.setAttr(Balloon_shd+'.KsssColor', 1, 0.77, 0.912, type='double3')
		cmds.setAttr(Balloon_shd+'.Ksss',  0.4)
	
	#Car paint(자동차쉐이더)
	def CarPaint_shd_Edit(self, *args):
		CarPaint_shd = cmds.shadingNode('aiStandard', n = 'CarPaint' , asShader=True)
		cmds.setAttr(CarPaint_shd+'.color',1, 0, 0, type='double3')
		cmds.setAttr(CarPaint_shd+'.Ks', 1)
		cmds.setAttr(CarPaint_shd+'.specularRoughness', 0)
		cmds.setAttr(CarPaint_shd+'.specularFresnel', 1)
		cmds.setAttr(CarPaint_shd+'.Ksn',  0.02)
		cmds.setAttr(CarPaint_shd+'.Fresnel', 1)
		cmds.setAttr(CarPaint_shd+'.KsssColor', 0.5, 0, 0, type='double3')
		cmds.setAttr(CarPaint_shd+'.Ksss',  0.163)
	
	#ceramic (도자기 쉐이더)
	def Ceramic_shd_Edit(self, *args):
		Ceramic_shd = cmds.shadingNode('aiStandard', n = 'Ceramic' , asShader=True)
		cmds.setAttr(Ceramic_shd+'.Ks', 0.65)
		cmds.setAttr(Ceramic_shd+'.specularRoughness', 0)
		cmds.setAttr(Ceramic_shd+'.specularFresnel', 1)
		cmds.setAttr(Ceramic_shd+'.Ksn',  0.1)
		cmds.setAttr(Ceramic_shd+'.Ksss',  0.3)
	
	#chocolate(초코렛 쉐이더)
	def Chocolate_shd_Edit(self, *args):
		Chocolate_shd = cmds.shadingNode('aiStandard', n = 'Chocolate' , asShader=True)
		cmds.setAttr(Chocolate_shd+'.color',0.385, 0.273, 0.212, type='double3')
		cmds.setAttr(Chocolate_shd+'.Kd', 1)
		cmds.setAttr(Chocolate_shd+'.diffuseRoughness', 0.376)
		cmds.setAttr(Chocolate_shd+'.Ks', 0.2)
		cmds.setAttr(Chocolate_shd+'.specularRoughness', 0.3)
		cmds.setAttr(Chocolate_shd+'.specularFresnel', 1)
		cmds.setAttr(Chocolate_shd+'.Ksn',  0.125)
		cmds.setAttr(Chocolate_shd+'.Kr', 0.1)
		cmds.setAttr(Chocolate_shd+'.Fresnel', 1)
		cmds.setAttr(Chocolate_shd+'.Krn',  0.1)
		cmds.setAttr(Chocolate_shd+'.KsssColor',0.592, 0.247, 0.122, type='double3')
		cmds.setAttr(Chocolate_shd+'.Ksss',  0.05)
		
	#chrome	(금속쉐이더)
	def chrome_shd_Edit(self, *args):
		chrome_shd = cmds.shadingNode('aiStandard', n = 'chrome' , asShader=True)
		cmds.setAttr(chrome_shd+'.Kd', 0)
		cmds.setAttr(chrome_shd+'.Ks', 1)
		cmds.setAttr(chrome_shd+'.specularRoughness', 0)
		cmds.setAttr(chrome_shd+'.specularFresnel', 1)
		cmds.setAttr(chrome_shd+'.Ksn',  0.732)
	
	#Clay(진흙쉐이더)
	def Clay_shd_Edit(self, *args):
		Clay_shd = cmds.shadingNode('aiStandard', n = 'Clay' , asShader=True)
		cmds.setAttr(Clay_shd+'.color',0.592, 0.247, 0.122, type='double3')
		cmds.setAttr(Clay_shd+'.Kd', 1)
		cmds.setAttr(Clay_shd+'.diffuseRoughness', 0.5)
		cmds.setAttr(Clay_shd+'.Ks', 0.3)
		cmds.setAttr(Clay_shd+'.specularRoughness', 0.5)
		cmds.setAttr(Clay_shd+'.specularFresnel', 1)
		cmds.setAttr(Clay_shd+'.Ksn',  0.125)
		cmds.setAttr(Clay_shd+'.KsssColor',0.592, 0.247, 0.122, type='double3')
		cmds.setAttr(Clay_shd+'.Ksss',  0.05)
		
		Clay_noise = cmds.shadingNode('noise', n = 'ClayNoise' , asTexture=True)
		cmds.setAttr(Clay_noise+'.frequency',16)
		Clay_bump_noise = cmds.shadingNode('bump2d', n = 'bumpNoise' , asUtility=True)
		cmds.connectAttr(Clay_noise+'.outAlpha',Clay_bump_noise+'.bumpValue')
		cmds.setAttr(Clay_bump_noise+'.bumpDepth',0.04)
		
		
		cmds.connectAttr(Clay_bump_noise+'.outNormal',Clay_shd+'.normalCamera')
	
	#glass(유리쉐이더)
	def Glass_shd_Edit(self, *args):
		Glass_shd = cmds.shadingNode('aiStandard', n = 'Glass' , asShader=True)
		cmds.setAttr(Glass_shd+'.color',0,0,0, type='double3')
		cmds.setAttr(Glass_shd+'.Kd', 0)
		cmds.setAttr(Glass_shd+'.Ks', 0)
		cmds.setAttr(Glass_shd+'.specularFresnel', 1)
		cmds.setAttr(Glass_shd+'.Kt',  1)
		cmds.setAttr(Glass_shd+'.IOR',1.175)
		cmds.setAttr(Glass_shd+'.FresnelUseIOR', 1)
	#gold (금쉐이더)
	def Gold_shd_Edit(self, *args):
		Gold_shd = cmds.shadingNode('aiStandard', n = 'Gold' , asShader=True)
		cmds.setAttr(Gold_shd+'.color',0.831, 0.472, 0, type='double3')
		cmds.setAttr(Gold_shd+'.diffuseRoughness', 0.427)
		cmds.setAttr(Gold_shd+'.KsColor',1, 0.864, 0.68, type='double3')
		cmds.setAttr(Gold_shd+'.Ks', 0.756)
		cmds.setAttr(Gold_shd+'.specularRoughness', 0.439)
		cmds.setAttr(Gold_shd+'.specularFresnel',  1)
		cmds.setAttr(Gold_shd+'.Ksn',1)
		
	#incandescent(백열전구쉐이더)
	def Incandescent_shd_Edit(self, *args):
		Incandescent_shd = cmds.shadingNode('aiStandard', n = 'Grow' , asShader=True)
		cmds.setAttr(Incandescent_shd+'.color',0,0,0, type='double3')
		cmds.setAttr(Incandescent_shd+'.Kd',0)
		cmds.setAttr(Incandescent_shd+'.KsColor',0,0,0, type='double3')
		cmds.setAttr(Incandescent_shd+'.Ks', 0.756)
		cmds.setAttr(Incandescent_shd+'.specularRoughness', 0)
		cmds.setAttr(Incandescent_shd+'.emission',  1)
		
	#matt(무광)
	def Matt_shd_Edit(self, *args):
		Matt_shd = cmds.shadingNode('aiStandard', n = 'Matt' , asShader=True)
		cmds.setAttr(Matt_shd+'.diffuseRoughness',1)
		cmds.setAttr(Matt_shd+'.specularRoughness', 0)
	
	#matt plastic (매트플라스틱쉐이더)
	def MattPlastic_shd_Edit(self, *args):
		MattPlastic_shd = cmds.shadingNode('aiStandard', n = 'MattPlastic' , asShader=True)
		cmds.setAttr(MattPlastic_shd+'.color',0,0,0, type='double3')
		cmds.setAttr(MattPlastic_shd+'.KsColor',0.538,0.538,0.538, type='double3')
		cmds.setAttr(MattPlastic_shd+'.Ks',0.265)
		cmds.setAttr(MattPlastic_shd+'.specularRoughness', 0.573)
	
	#MetallicCarPaint(금속 자동차쉐이더)
	def MetallicCarPaint_shd_Edit(self, *args):
		MetallicCarPaint_shd = cmds.shadingNode('aiStandard', n = 'MetallicCarPaint' , asShader=True)
		cmds.setAttr(MetallicCarPaint_shd+'.color', 0.202, 0.466, 1, type='double3')
		cmds.setAttr(MetallicCarPaint_shd+'.KsColor',0.579, 0.944, 1 , type='double3')
		cmds.setAttr(MetallicCarPaint_shd+'.Ks',0.45)
		cmds.setAttr(MetallicCarPaint_shd+'.specularRoughness', 0.5)
		cmds.setAttr(MetallicCarPaint_shd+'.specularFresnel', 1)
		cmds.setAttr(MetallicCarPaint_shd+'.Ksn', 0.4)
		cmds.setAttr(MetallicCarPaint_shd+'.Fresnel', 1)
	
	#plasticToy (플라스틱장난감쉐이더)
	def plasticToy_shd_Edit(self, *args):
		plasticToy_shd = cmds.shadingNode('aiStandard', n = 'plasticToy' , asShader=True)
		cmds.setAttr(plasticToy_shd+'.color', 0.264, 0.539, 0.326, type='double3')
		cmds.setAttr(plasticToy_shd+'.KsColor', 0.785, 0.785, 0.785 , type='double3')
		cmds.setAttr(plasticToy_shd+'.Ks',0.24)
		cmds.setAttr(plasticToy_shd+'.specularRoughness', 0.4)
		cmds.setAttr(plasticToy_shd+'.specularFresnel', 1)
		cmds.setAttr(plasticToy_shd+'.Ksn', 0.675)
		cmds.setAttr(plasticToy_shd+'.specularFresnel', 1)
		cmds.setAttr(plasticToy_shd+'.KsssColor',0.254, 0.549, 0.326, type='double3')
		cmds.setAttr(plasticToy_shd+'.Ksss', 0.1)
		
	#ShinyPlastic(반짝이는쉐이더)
	def ShinyPlastic_shd_Edit(self, *args):
		ShinyPlastic_shd = cmds.shadingNode('aiStandard', n = 'ShinyPlastic' , asShader=True)
		cmds.setAttr(ShinyPlastic_shd+'.color',0,0,0, type='double3')
		cmds.setAttr(ShinyPlastic_shd+'.diffuseRoughness',0.214)
		cmds.setAttr(ShinyPlastic_shd+'.KsColor', 0.618, 0.618, 0.618 , type='double3')
		cmds.setAttr(ShinyPlastic_shd+'.Ks',0.537)
		cmds.setAttr(ShinyPlastic_shd+'.specularRoughness', 0.358)
		cmds.setAttr(ShinyPlastic_shd+'.specularFresnel', 1)
		cmds.setAttr(ShinyPlastic_shd+'.Ksn', 0.675)
		cmds.setAttr(ShinyPlastic_shd+'.specularFresnel', 1)
		cmds.setAttr(ShinyPlastic_shd+'.Ksn', 0.7)
	
	#SilkMattPlastic_A(무광실크 플라스틱A)
	def SilkMattP_A_shd_Edit(self, *args):
		SilkMattP_A_shd = cmds.shadingNode('aiStandard', n = 'SilkMattPlastic_A' , asShader=True)
		cmds.setAttr(SilkMattP_A_shd+'.color',0,0,0, type='double3')
		cmds.setAttr(SilkMattP_A_shd+'.diffuseRoughness',1)
		cmds.setAttr(SilkMattP_A_shd+'.Ks', 0.756)
		cmds.setAttr(SilkMattP_A_shd+'.specularRoughness', 0.789)
	
	#SilkMattPlastic_B(무광실크 플라스틱B)
	def SilkMattP_B_shd_Edit(self, *args):
		SilkMattP_B_shd = cmds.shadingNode('aiStandard', n = 'SilkMattPlastic_B' , asShader=True)
		cmds.setAttr(SilkMattP_B_shd+'.color',0,0,0, type='double3')
		cmds.setAttr(SilkMattP_B_shd+'.Ks', 0.317)
		cmds.setAttr(SilkMattP_B_shd+'.specularRoughness', 0.642)
	
	#SoftPlastic(부드러운플라스틱)
	def SoftPlastic_shd_Edit(self, *args):
		SoftPlastic_shd = cmds.shadingNode('aiStandard', n = 'SoftPlastic' , asShader=True)
		cmds.setAttr(SoftPlastic_shd+'.color',0.9, 0.9, 0.9, type='double3')
		cmds.setAttr(SoftPlastic_shd+'.diffuseRoughness', 0.5)
		cmds.setAttr(SoftPlastic_shd+'.KsColor',0.265, 0.265, 0.265, type='double3')
		cmds.setAttr(SoftPlastic_shd+'.Ks', 0.4)
		cmds.setAttr(SoftPlastic_shd+'.specularRoughness', 0.67)
		cmds.setAttr(SoftPlastic_shd+'.KsssColor',1, 0.755, 0.3, type='double3')
		cmds.setAttr(SoftPlastic_shd+'.Ksss', 0.4)
	
	#Styrofoam(스티로폼)
	def Styrofoam_shd_Edit(self, *args):
		Styrofoam_shd = cmds.shadingNode('aiStandard', n = 'Styrofoam' , asShader=True)
		cmds.setAttr(Styrofoam_shd+'.diffuseRoughness', 0.513)
		cmds.setAttr(Styrofoam_shd+'.Ks', 0.444)
		cmds.setAttr(Styrofoam_shd+'.specularRoughness', 0.821)
		cmds.setAttr(Styrofoam_shd+'.specularFresnel', 1)
		cmds.setAttr(Styrofoam_shd+'.Ksn', 0.085)
		
		Styrofoam_noise = cmds.shadingNode('noise', n = 'StyrofoamNoise' , asTexture=True)
		cmds.setAttr(Styrofoam_noise+'.frequency',70)
		Styrofoam_bump_noise = cmds.shadingNode('bump2d', n = 'StyrofoamNoise' , asUtility=True)
		cmds.connectAttr(Styrofoam_noise+'.outAlpha',Styrofoam_bump_noise+'.bumpValue')
		cmds.setAttr(Styrofoam_bump_noise+'.bumpDepth',0.05)
	
		cmds.connectAttr(Styrofoam_bump_noise+'.outNormal',Styrofoam_shd+'.normalCamera')
	
	#TableCloth(테이블보 재질)
	def TableCloth_shd_Edit(self, *args):
		#재질
		TableCloth_shd = cmds.shadingNode('aiStandard', n = 'TableCloth' , asShader=True)
		cmds.setAttr(TableCloth_shd+'.Kd', 0.8)
		cmds.setAttr(TableCloth_shd+'.diffuseRoughness', 1)
		#2d범프맵
		TableCloth_colth = cmds.shadingNode('cloth', n = 'TableCloth' , asTexture=True)
		#2d텍스처맵
		TableCloth_place2dTexture = cmds.shadingNode('place2dTexture', n = 'TableClothPlace2dTexture' , asUtility=True)
		cmds.setAttr(TableCloth_place2dTexture+'.repeatU',40)
		cmds.setAttr(TableCloth_place2dTexture+'.repeatV',40)
		#범프와텍스처연결하기
		cmds.connectAttr(TableCloth_place2dTexture+'.outUV',TableCloth_colth+'.uvCoord')
		#2d범프만들기 
		TableCloth_bump = cmds.shadingNode('bump2d', n = 'TableClothBump' , asUtility=True)
		cmds.setAttr(TableCloth_bump+'.bumpDepth',0.05)
		#범프와 텍스처연결하기
		cmds.connectAttr(TableCloth_colth+'.outAlpha',TableCloth_bump+'.bumpValue')
		#범프와 재질연결하기
		cmds.connectAttr( TableCloth_bump+'.outNormal' , TableCloth_shd+'.normalCamera' )
	
		#디퓨즈컬러 만들기
		TableCloth_dif = cmds.shadingNode('checker', n = 'TableClothDif' , asTexture=True)
		cmds.setAttr(TableCloth_dif+'.color2', 1, 0.8, 0.8 ,type =  'double3' )
		cmds.setAttr(TableCloth_dif+'.color1', 1, 0.3, 0.3 ,type =  'double3' )
		#2d텍스처맵
		TableCloth_Dif_place2dTexture = cmds.shadingNode('place2dTexture', n = 'TableClothDifPlace2dTexture' , asUtility=True)
		cmds.setAttr(TableCloth_Dif_place2dTexture+'.repeatU',4)
		cmds.setAttr(TableCloth_Dif_place2dTexture+'.repeatV',4)
	
		cmds.connectAttr(TableCloth_Dif_place2dTexture+'.outUV',TableCloth_dif+'.uvCoord')
		#쉐이더와디퓨즈연결
		cmds.connectAttr(TableCloth_dif+'.outColor',TableCloth_shd+'.color')
	
	#Velvet(벨벳재질,겨울철옷재질)(러프니스에 텍스처맵넣을때는 텍스처에 알파일루미네이션꼭켜야한다!)
	def Velvet_shd_Edit(self, *args):
		Velvet_shd = cmds.shadingNode('aiStandard', n = 'Velvet' , asShader=True)
		cmds.setAttr(Velvet_shd+'.color',0.369, 0.56, 0.917, type='double3')
		Velvet_fractal = cmds.shadingNode('fractal', n = 'VelvetFractal' , asTexture=True)
		cmds.setAttr(Velvet_fractal+'.ratio',1)
		#텍스처에 알파일루미네이션켜기
		cmds.setAttr(Velvet_fractal+'.alphaIsLuminance',1)
		Velvet_place2dTexture = cmds.shadingNode('place2dTexture', n = 'VelvetPlace2dTexture' , asUtility=True)
		cmds.connectAttr(Velvet_place2dTexture+'.outUV',Velvet_fractal+'.uvCoord')
		cmds.connectAttr(Velvet_fractal+'.outAlpha ',Velvet_shd+'.diffuseRoughness')
		cmds.connectAttr(Velvet_fractal+'.outAlpha ',Velvet_shd+'.specularRoughness')
	
	#Wall_Plaster (석고재질)
	def WallPlaster_shd_Edit(self, *args):
		WallPlaster_shd = cmds.shadingNode('aiStandard', n = 'WallPlaster' , asShader=True)
		cmds.setAttr(WallPlaster_shd+'.diffuseRoughness',1)
		cmds.setAttr(WallPlaster_shd+'.Ks',0.126)
		cmds.setAttr(WallPlaster_shd+'.specularRoughness',0.766)
	
		WallPlaster_bump = cmds.shadingNode('bump2d', n = 'WallPlasterBump' , asUtility=True)
		cmds.setAttr(WallPlaster_bump+'.bumpDepth',0.2)
		WallPlaster_noise = cmds.shadingNode('noise', n = 'WallPlasterNoise' , asTexture=True)
		cmds.setAttr(WallPlaster_noise+'.invert',1)
		cmds.setAttr(WallPlaster_noise+'.threshold',0.17)
		cmds.setAttr(WallPlaster_noise+'.amplitude',1)
		cmds.setAttr(WallPlaster_noise+'.ratio',0.89)
		cmds.setAttr(WallPlaster_noise+'.frequencyRatio',2.1)
		cmds.setAttr(WallPlaster_noise+'.frequency',7)
	
		cmds.connectAttr( WallPlaster_noise+'.outAlpha' , WallPlaster_bump+'.bumpValue' )
		cmds.connectAttr( WallPlaster_bump+'.outNormal' , WallPlaster_shd+'.normalCamera' )
	
	#Wax(밀랍인형재질)
	def Wax_shd_Edit(self, *args):
		Wax_shd = cmds.shadingNode('aiStandard', n = 'Wax' , asShader=True)
		cmds.setAttr(Wax_shd+'.color',0.9, 0.9, 0.9, type='double3')
		cmds.setAttr(Wax_shd+'.Kd',0.3)
		cmds.setAttr(Wax_shd+'.diffuseRoughness',0.53)
		cmds.setAttr(Wax_shd+'.Ks',0.547)
		cmds.setAttr(Wax_shd+'.specularRoughness',0.6)
		cmds.setAttr(Wax_shd+'.specularFresnel',1)
		cmds.setAttr(Wax_shd+'.Ksss',0.573)
	
	#WheelRims(자동차바퀴재질)
	def WheelRims_shd_Edit(self, *args):
		WheelRims_shd = cmds.shadingNode('aiStandard', n = 'WheelRims' , asShader=True)
		cmds.setAttr(WheelRims_shd+'.color',0.671, 0.671, 0.671, type='double3')
		cmds.setAttr(WheelRims_shd+'.Kd',0.2)
		cmds.setAttr(WheelRims_shd+'.Ks',0.8)
		cmds.setAttr(WheelRims_shd+'.specularRoughness',0.3)
	
	#Water재질
	
	def Water_shd_Edit(self, *args):
		Water_shd = cmds.shadingNode('aiStandard', n = 'Water' , asShader=True)
		cmds.setAttr(Water_shd+'.Kd',0.325)
		cmds.setAttr(Water_shd+'.Kb',0.1)
		cmds.setAttr(Water_shd+'.specularRoughness',0)
		cmds.setAttr(Water_shd+'.specularFresnel',1)
		cmds.setAttr(Water_shd+'.Ksn',0.1)
		cmds.setAttr(Water_shd+'.Kt',0.9)
		cmds.setAttr(Water_shd+'.IOR',1.33)
		cmds.setAttr(Water_shd+'.FresnelUseIOR',1)
		cmds.setAttr(Water_shd+'.sssRadius',1,1,1, type='double3')
	
	#TransparentPlastic 투명플라스틱재질
	def TransparentPlastic_shd_Edit(self, *args):
		TransparentPlastic_shd = cmds.shadingNode('aiStandard', n = 'TransparentPlastic' , asShader=True)
		cmds.setAttr(TransparentPlastic_shd+'.Kd',0)
		cmds.setAttr(TransparentPlastic_shd+'.Kb',0)
		cmds.setAttr(TransparentPlastic_shd+'.specularRoughness',0)
		cmds.setAttr(TransparentPlastic_shd+'.specularFresnel',1)
		cmds.setAttr(TransparentPlastic_shd+'.Ks',1)
		cmds.setAttr(TransparentPlastic_shd+'.Kt',1)
		cmds.setAttr(TransparentPlastic_shd+'.IOR',1.4)
		cmds.setAttr(TransparentPlastic_shd+'.FresnelUseIOR',1)
		
	#bubbl_쉐이더
	def Bubbl_shd_Edit(self, *args):
		#기본shader만들기 
		Bubbl_shd = cmds.shadingNode('aiStandard', n = 'Bubbl' , asShader=True)
		cmds.setAttr(Bubbl_shd+'.color',0.643, 0.643, 0.643, type='double3')
		cmds.setAttr(Bubbl_shd+'.specularRoughness',0)
		cmds.setAttr(Bubbl_shd+'.specularFresnel',1)
		cmds.setAttr(Bubbl_shd+'.Kd',0)
		cmds.setAttr(Bubbl_shd+'.Ks',1)
		cmds.setAttr(Bubbl_shd+'.Kr',1)
		cmds.setAttr(Bubbl_shd+'.Ksn',0.086)
		cmds.setAttr(Bubbl_shd+'.Fresnel',1)
		cmds.setAttr(Bubbl_shd+'.Krn',0.22)
		cmds.setAttr(Bubbl_shd+'.Kt',1)
		cmds.setAttr(Bubbl_shd+'.IOR',1.005)
	
		#remapHsv //명암을 참고로 Hue Saturation Value로 변경
		Bubbl_remapHsv = cmds.shadingNode('remapHsv', n = 'BubblRemapHsv' ,asUtility=True)
		cmds.setAttr(Bubbl_remapHsv+'.value[1].value_Position', 0.58)
		cmds.setAttr(Bubbl_remapHsv+'.value[1].value_FloatValue', 1)
	
	
		#fluidTexture2D 스펙큘러의 컬러를 적용할노드
		Bubbl_fluidTexture2D = cmds.shadingNode('fluidTexture2D', n = 'BubblFluidTexture2D' , asTexture=True)
		#기본설정
		cmds.setAttr(Bubbl_fluidTexture2D+'.squareVoxels',1)
		cmds.setAttr(Bubbl_fluidTexture2D+'.boundaryY',2)
		cmds.setAttr(Bubbl_fluidTexture2D+'.squareVoxels',1)
		cmds.setAttr(Bubbl_fluidTexture2D+'.dimensionsW',12)
		cmds.setAttr(Bubbl_fluidTexture2D+'.dimensionsH',8)
		cmds.setAttr(Bubbl_fluidTexture2D+'.boundaryX',4)
		cmds.setAttr(Bubbl_fluidTexture2D+'.colorInputBias',0.597)
		cmds.setAttr(Bubbl_fluidTexture2D+'.highDetailSolve',3)
		cmds.setAttr(Bubbl_fluidTexture2D+'.alphaGain',2)
		cmds.setAttr(Bubbl_fluidTexture2D+'.densityScale',0.5)
		cmds.setAttr(Bubbl_fluidTexture2D+'.densityBuoyancy',1)
		cmds.setAttr(Bubbl_fluidTexture2D+'.densityScale',1)
		cmds.setAttr(Bubbl_fluidTexture2D+'.densityBuoyancy',-0.2)
		cmds.setAttr(Bubbl_fluidTexture2D+'.opacity[0].opacity_FloatValue',0.12)
		cmds.setAttr(Bubbl_fluidTexture2D+'.boundaryX',4)
		cmds.setAttr(Bubbl_fluidTexture2D+'.boundaryX',4)
		cmds.setAttr(Bubbl_fluidTexture2D+'.boundaryX',4)
		cmds.setAttr(Bubbl_fluidTexture2D+'.boundaryX',4)
		cmds.setAttr(Bubbl_fluidTexture2D+'.transparency',0,0,0, type='double3')
		cmds.setAttr(Bubbl_fluidTexture2D+'.turbulenceFrequency',1.052)
		cmds.setAttr(Bubbl_fluidTexture2D+'.turbulenceStrength',0.276)
		#스펙큘러에맻힐컬러
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[0].color_Position',0.061)
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[0].color_Color',0.216, 0.262, 0.41, type='double3')
	
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[2].color_Color', 0.141, 0.096, 1, type='double3')
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[2].color_Position',0.357)
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[2].color_Interp',1)
	
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[3].color_Color',0.31, 0.863, 1, type='double3')
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[3].color_Position',0.548)
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[3].color_Interp',1)
	
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[4].color_Color',0.489, 1, 0.489, type='double3')
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[4].color_Position',0.609)
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[4].color_Interp',1)
	
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[5].color_Color',1, 0.93, 0.157, type='double3')
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[5].color_Position',0.696)
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[5].color_Interp',1)
	
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[6].color_Color',1, 0.208, 0.208, type='double3')
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[6].color_Position',0.791)
		cmds.setAttr(Bubbl_fluidTexture2D+'.color[6].color_Interp',1)
	
	
		#time 노드
		Bubbl_time = cmds.shadingNode('time', n = 'BubblTime' , asUtility=True)
		#place2dTexture노드
		Bubbl_place2dTexture = cmds.shadingNode('place2dTexture', n = 'BubblPlace2dTexture' , asUtility=True)
	
		#애니메이션 주는노드 animCurveTU
		Bubbl_animCurveTU = cmds.shadingNode('animCurveTU', n = 'BubblAnimCurveTU' , asUtility=True)
	
		#노드연결하기
		cmds.connectAttr(Bubbl_remapHsv+'.outColor',Bubbl_shd+'.KsColor')
		cmds.connectAttr(Bubbl_fluidTexture2D+'.outColor',Bubbl_remapHsv+'.color')
		cmds.connectAttr(Bubbl_place2dTexture+'.outUV',Bubbl_fluidTexture2D+'.uvCoord')
		cmds.connectAttr(Bubbl_place2dTexture+'.outUvFilterSize',Bubbl_fluidTexture2D+'.uvFilterSize')
		cmds.connectAttr(Bubbl_time+'.outTime',Bubbl_fluidTexture2D+'.currentTime')	
	
	
	#나무쉐이더
	def Wood_shd_Edit(self, *args):
		#Wood쉐이더
		Wood_shd = cmds.shadingNode('aiStandard', n = 'Wood' , asShader=True)
		cmds.setAttr(Wood_shd+'.diffuseRoughness',0.709)
		cmds.setAttr(Wood_shd+'.specularRoughness',1)
		cmds.setAttr(Wood_shd+'.specularFresnel',1)
		
		#나무디퓨즈
		Wood_dif = cmds.shadingNode('fractal', n = 'Wood_dif' , asTexture=True)
		cmds.setAttr(Wood_dif+'.frequencyRatio',1.4)
		cmds.setAttr(Wood_dif+'.defaultColor',0.824, 0.627, 0.471, type='double3')
		cmds.setAttr(Wood_dif+'.colorGain',0.157, 0.078, 0.039, type='double3')
		cmds.setAttr(Wood_dif+'.colorOffset',0.090, 0.045, 0.022, type='double3')
			
		Wood_place2dTexture_A = cmds.shadingNode('place2dTexture', n = 'BubblPlace2dTexture_A' , asUtility=True)
	
		cmds.connectAttr(Wood_place2dTexture_A+'.outUV',Wood_dif+'.uvCoord')
		cmds.connectAttr(Wood_place2dTexture_A+'.outUvFilterSize',Wood_dif+'.uvFilterSize')
	
	
		#스페큘러,러프니스,범프
		Wood_spc_rf_bump = cmds.shadingNode('fractal', n = 'Wood_spc_rf_bump' , asTexture=True)
		cmds.setAttr(Wood_spc_rf_bump+'.frequencyRatio',1.4)
	
		Wood_place2dTexture_B = cmds.shadingNode('place2dTexture', n = 'BubblPlace2dTexture_B' , asUtility=True)
	
		cmds.connectAttr(Wood_place2dTexture_B+'.outUV',Wood_spc_rf_bump+'.uvCoord')
		cmds.connectAttr(Wood_place2dTexture_B+'.outUvFilterSize',Wood_spc_rf_bump+'.uvFilterSize')
	
		#연결
		cmds.connectAttr(Wood_dif+'.outColor',Wood_shd+'.color')
		cmds.connectAttr(Wood_spc_rf_bump+'.outColor',Wood_shd+'.KsColor')
		cmds.connectAttr(Wood_spc_rf_bump+'.outAlpha',Wood_shd+'.Ks')
	
		Wood_bump = cmds.createNode('bump2d', n = 'WoodBump' , skipSelect=True)
		cmds.setAttr(Wood_bump+'.bumpDepth',0.1)
	
		cmds.connectAttr(Wood_spc_rf_bump+'.outAlpha',Wood_bump+'.bumpValue')
		cmds.connectAttr(Wood_bump+'.outNormal',Wood_shd+'.normalCamera')
	
	#facingRatio 쉐이더
	def facingRatio_shd_Edit(self, *args):
		facingRatio_shd = cmds.shadingNode('aiStandard',n='FacingRatio', asShader=True)
		king_aiInfo = cmds.shadingNode('samplerInfo',n='facingRatiosamplerInfo', asUtility=True)
		king_Ramp = cmds.shadingNode('ramp',n='facingRatioRamp', asTexture=True)
	
		cmds.select(king_Ramp,  r = 1 )
		king_Ramp_del = cmds.ls(selection=True,type = 'ramp')
		#print king_Ramp_del
		for rmove in king_Ramp_del:
			#print rmove
			cmds.setAttr(rmove+'.colorEntryList[0].color' ,0.9 ,0.9, 0.9, type = 'double3' )
			cmds.removeMultiInstance(rmove+'.colorEntryList[1]', b = 1 )
			cmds.setAttr(rmove+'.colorEntryList[2].color' ,0 ,0, 0, type = 'double3' )
			cmds.setAttr(rmove+'.colorEntryList[2].position' ,1)
			cmds.setAttr(rmove+'.interpolation' ,4)
		
		cmds.connectAttr(king_aiInfo+'.facingRatio' , king_Ramp+'.uvCoord.uCoord' )
		cmds.connectAttr(king_aiInfo+'.facingRatio' , king_Ramp+'.uvCoord.vCoord' )
		cmds.connectAttr(king_Ramp+'.outColor' , facingRatio_shd+'.color' )
	
	#림쉐이더
	def Rim_shd_Edit(self, *args):
		#쉐이더
		Rim_shd = cmds.shadingNode('aiStandard', n = 'RimShd' , asShader=True)
		cmds.setAttr(Rim_shd+'.diffuseRoughness',1)
		cmds.setAttr(Rim_shd+'.specularRoughness',0)
		#컬러브렌더
		Rim_ColorBlend = cmds.shadingNode('blendColors', n = 'RimColorBlend' , asUtility = True)
		cmds.setAttr(Rim_ColorBlend+'.color2',1,1,1, type = 'double3')
		#림램프
		Rim_Ramp = cmds.shadingNode('ramp', n = 'RimRamp' , asTexture = True)
		cmds.setAttr(Rim_Ramp+'.interpolation',3)
		#cmds.removeMultiInstance((Rim_Ramp+'.colorEntryList[1]', b=True )
		cmds.setAttr(Rim_Ramp+'.colorEntryList[0].color' , 1,1,1, type = 'double3')
		cmds.setAttr(Rim_Ramp+'.colorEntryList[2].position' ,1)
		cmds.setAttr(Rim_Ramp+'.colorEntryList[2].color' , 0.955, 0.694, 0.384, type = 'double3')
		#클램프
		Rim_clamp = cmds.shadingNode('clamp', n = 'Rimclamp' , asUtility = True)
		cmds.setAttr(Rim_clamp+'.maxR' ,1)
		#샘플인포
		Rim_samplerInfo = cmds.shadingNode('samplerInfo', n = 'RimSamplerInfo' , asUtility = True)
		#연결
		cmds.connectAttr(Rim_ColorBlend+'.output ',Rim_shd+'.color')
		cmds.connectAttr(Rim_Ramp+'.outColor ',Rim_ColorBlend+'.color1')
		cmds.connectAttr(Rim_clamp+'.outputR ',Rim_Ramp+'.vCoord')
		cmds.connectAttr(Rim_clamp+'.outputR ',Rim_ColorBlend+'.blender')
		cmds.connectAttr(Rim_samplerInfo+'.facingRatio ',Rim_clamp+'.inputR')
	
	#Wire 쉐이더
	def Wire_shd_Edit(self, *args):
		Wire_shd = cmds.shadingNode('aiUtility', n = 'Wire' , asShader=True)
		cmds.setAttr(Wire_shd+'.colorMode' ,14)
	
	
	
	#Obq_toon_쉐이더
	def ObqToon_Edit(self, *args):
		Obq_aiUtility = cmds.shadingNode('aiUtility', n = 'ObqaiUtility' , asShader=True)
		cmds.setAttr(Obq_aiUtility+'.shadeMode',2)
	
		Obq_toon_shd = cmds.shadingNode('aiObqToonSimple', n = 'ObqToonShd' , asShader=True)
		cmds.setAttr(Obq_toon_shd+'.ambientColor',0 ,0 , 1, type = 'double3' )
		cmds.setAttr(Obq_toon_shd+'.ambientScale',0.5 )
		cmds.setAttr(Obq_toon_shd+'.diffuseScale',0.75 )
		cmds.setAttr(Obq_toon_shd+'.diffuseSoftness',0.05)
		cmds.setAttr(Obq_toon_shd+'.highlightScale',1)
		cmds.setAttr(Obq_toon_shd+'.highlightExponent',30)
		cmds.setAttr(Obq_toon_shd+'.highlightCoverage',0.2)
		cmds.setAttr(Obq_toon_shd+'.highlightSoftness',0)
		cmds.setAttr(Obq_toon_shd+'.rimlightScale',5)
		cmds.setAttr(Obq_toon_shd+'.rimlightCoverage',0.6)
		cmds.setAttr(Obq_toon_shd+'.rimlightSoftness',0.05)
		cmds.setAttr(Obq_toon_shd+'.rimlightColor',0 ,0 , 0.068, type = 'double3' )
	
		Obq_checker = cmds.shadingNode('checker', n = 'ObqChecker' , asTexture=True)
		cmds.setAttr(Obq_checker+'.color1',0.526 , 0.466 ,1, type = 'double3' )
		cmds.setAttr(Obq_checker+'.color2',0.191 ,0.191 ,1 , type = 'double3' )
	
		Obq_place2dTexture = cmds.shadingNode('place2dTexture', n = 'Obqplace2dTexture' , asUtility=True)
		cmds.setAttr(Obq_place2dTexture+'.repeatU',4)
		cmds.setAttr(Obq_place2dTexture+'.repeatV',4)
		cmds.connectAttr(Obq_place2dTexture+'.outUV',Obq_checker+'.uvCoord')
		cmds.connectAttr(Obq_place2dTexture+'.outUvFilterSize',Obq_checker+'.uvFilterSize')
	
		cmds.connectAttr(Obq_toon_shd+'.outColor',Obq_aiUtility+'.color')
		cmds.connectAttr(Obq_checker+'.outColor',Obq_toon_shd+'.diffuseColor')
	
	
	#toon_A 쉐이더 
	def Toon_A_Edit(self, *args):
		Toon_A_shd = cmds.shadingNode('aiUtility', n = 'Toon_A' , asShader=True)
		cmds.setAttr(Toon_A_shd+'.shadeMode',2)
	
		Toon_A_ramp = cmds.shadingNode('ramp', n = 'ToonARamp' , asTexture=True)
		cmds.setAttr(Toon_A_ramp+'.interpolation',0)
		cmds.removeMultiInstance(Toon_A_ramp+'.colorEntryList[2]' , b=1 )
		cmds.setAttr(Toon_A_ramp+'.colorEntryList[0].color',0,0,0.908, type = 'double3')
	
		Toon_A_samplerInfo = cmds.shadingNode('samplerInfo', n = 'ToonA_samplerInfo' , asUtility = True)
		cmds.connectAttr(Toon_A_samplerInfo+'.facingRatio',Toon_A_ramp+'.uCoord')
		cmds.connectAttr(Toon_A_samplerInfo+'.facingRatio',Toon_A_ramp+'.vCoord')
	
		Toon_A_layered = cmds.shadingNode('layeredShader', n = 'Toon_ALayered' , asShader=True)
		
		Toon_A_Spc = cmds.shadingNode('aiStandard', n = 'Toon_ASpc' , asShader=True)
		cmds.setAttr(Toon_A_Spc+'.color',0,0,0, type = 'double3')
		cmds.setAttr(Toon_A_Spc+'.Kd',0)
		cmds.setAttr(Toon_A_Spc+'.Ks',1)
		cmds.setAttr(Toon_A_Spc+'.specularRoughness', 0.219)
		cmds.setAttr(Toon_A_Spc+'.directDiffuse',0)
		cmds.setAttr(Toon_A_Spc+'.indirectDiffuse',0)
		cmds.setAttr(Toon_A_Spc+'.directSpecular',1)
		cmds.setAttr(Toon_A_Spc+'.indirectSpecular',0)
		
		Toon_A_Dif = cmds.shadingNode('aiUtility', n = 'Toon_ADif' , asShader=True)
		cmds.setAttr(Toon_A_Dif+'.shadeMode',2)
	
		Toon_A_checker = cmds.shadingNode('checker', n = 'Toon_AChecker' , asTexture=True)
		cmds.setAttr(Toon_A_checker+'.color1',0.668 , 0.652 ,1, type = 'double3' )
		cmds.setAttr(Toon_A_checker+'.color2',0.270 ,0.270 ,1 , type = 'double3' )
	
		Toon_A_place2dTexture = cmds.shadingNode('place2dTexture', n = 'Toon_Alace2dTexture' , asUtility=True)
		cmds.setAttr(Toon_A_place2dTexture+'.repeatU',4)
		cmds.setAttr(Toon_A_place2dTexture+'.repeatV',4)
		cmds.connectAttr(Toon_A_place2dTexture+'.outUV',Toon_A_checker+'.uvCoord')
		cmds.connectAttr(Toon_A_place2dTexture+'.outUvFilterSize',Toon_A_checker+'.uvFilterSize')
		cmds.connectAttr(Toon_A_checker+'.outColor',Toon_A_Dif+'.color')
		cmds.connectAttr(Toon_A_Spc+'.outColor',Toon_A_layered+'.inputs[0].color')
		cmds.connectAttr(Toon_A_Dif+'.outColor',Toon_A_layered+'.inputs[1].color')
		cmds.setAttr(Toon_A_layered+'.inputs[0].transparency' , 1, 1, 1, type = 'double3')
		cmds.setAttr(Toon_A_layered+'.inputs[1].transparency' , 1, 1, 1, type = 'double3')
	
		cmds.setAttr(Toon_A_ramp+'.colorEntryList[1].position',0.595)
		cmds.connectAttr(Toon_A_layered+'.outColor',Toon_A_ramp+'.colorEntryList[1].color')
		cmds.connectAttr(Toon_A_ramp+'.outColor',Toon_A_shd+'.color')
	
	
	
	#toon_B 쉐이더
	def Toon_B_Edit(self, *args):
		
		Toon_B_shd = cmds.shadingNode('aiUtility', n = 'Toon_B' , asShader=True)
		cmds.setAttr(Toon_B_shd+'.shadeMode',2)
	
		Toon_B_ramp = cmds.shadingNode('ramp', n = 'ToonBRamp' , asTexture=True)
		cmds.setAttr(Toon_B_ramp+'.interpolation',0)
		cmds.removeMultiInstance(Toon_B_ramp+'.colorEntryList[2]' , b=1 )
		cmds.setAttr(Toon_B_ramp+'.colorEntryList[0].color',1,1,1, type = 'double3')
	
		Toon_B_samplerInfo = cmds.shadingNode('samplerInfo', n = 'ToonB_samplerInfo' , asUtility = True)
		cmds.connectAttr(Toon_B_samplerInfo+'.facingRatio',Toon_B_ramp+'.uCoord')
		cmds.connectAttr(Toon_B_samplerInfo+'.facingRatio',Toon_B_ramp+'.vCoord')
	
	
		Toon_B_Ami = cmds.shadingNode('aiStandard', n = 'Toon_BAmi' , asShader=True)
		cmds.setAttr(Toon_B_Ami+'.color',1,1,1, type = 'double3')
		cmds.setAttr(Toon_B_Ami+'.Kd',1)
		cmds.setAttr(Toon_B_Ami+'.specularRoughness',0)
		cmds.setAttr(Toon_B_Ami+'.directDiffuse', 20)
		cmds.setAttr(Toon_B_Ami+'.indirectDiffuse',0)
	
		cmds.setAttr(Toon_B_ramp+'.colorEntryList[1].position',0.595)
		cmds.connectAttr(Toon_B_Ami+'.outColor',Toon_B_ramp+'.colorEntryList[1].color')
		cmds.connectAttr(Toon_B_ramp+'.outColor',Toon_B_shd+'.color')
	
	
	#toon_AB 쉐이더
	def Toon_AB_Edit(self, *args):
		#A
		Toon_A_shd = cmds.shadingNode('aiUtility', n = 'Toon_A' , asShader=True)
		cmds.setAttr(Toon_A_shd+'.shadeMode',2)
	
		Toon_A_ramp = cmds.shadingNode('ramp', n = 'ToonARamp' , asTexture=True)
		cmds.setAttr(Toon_A_ramp+'.interpolation',0)
		cmds.removeMultiInstance(Toon_A_ramp+'.colorEntryList[2]' , b=1 )
		cmds.setAttr(Toon_A_ramp+'.colorEntryList[0].color',0,0,0.908, type = 'double3')
	
		Toon_A_samplerInfo = cmds.shadingNode('samplerInfo', n = 'ToonA_samplerInfo' , asUtility = True)
		cmds.connectAttr(Toon_A_samplerInfo+'.facingRatio',Toon_A_ramp+'.uCoord')
		cmds.connectAttr(Toon_A_samplerInfo+'.facingRatio',Toon_A_ramp+'.vCoord')
	
		Toon_A_layered = cmds.shadingNode('layeredShader', n = 'Toon_ALayered' , asShader=True)
		
		Toon_A_Spc = cmds.shadingNode('aiStandard', n = 'Toon_ASpc' , asShader=True)
		cmds.setAttr(Toon_A_Spc+'.color',0,0,0, type = 'double3')
		cmds.setAttr(Toon_A_Spc+'.Kd',0)
		cmds.setAttr(Toon_A_Spc+'.Ks',1)
		cmds.setAttr(Toon_A_Spc+'.specularRoughness', 0.219)
		cmds.setAttr(Toon_A_Spc+'.directDiffuse',0)
		cmds.setAttr(Toon_A_Spc+'.indirectDiffuse',0)
		cmds.setAttr(Toon_A_Spc+'.directSpecular',1)
		cmds.setAttr(Toon_A_Spc+'.indirectSpecular',0)
		
		Toon_A_Dif = cmds.shadingNode('aiUtility', n = 'Toon_ADif' , asShader=True)
		cmds.setAttr(Toon_A_Dif+'.shadeMode',2)
	
		Toon_A_checker = cmds.shadingNode('checker', n = 'Toon_AChecker' , asTexture=True)
		cmds.setAttr(Toon_A_checker+'.color1',0.668 , 0.652 ,1, type = 'double3' )
		cmds.setAttr(Toon_A_checker+'.color2',0.270 ,0.270 ,1 , type = 'double3' )
	
		Toon_A_place2dTexture = cmds.shadingNode('place2dTexture', n = 'Toon_Alace2dTexture' , asUtility=True)
		cmds.setAttr(Toon_A_place2dTexture+'.repeatU',4)
		cmds.setAttr(Toon_A_place2dTexture+'.repeatV',4)
		cmds.connectAttr(Toon_A_place2dTexture+'.outUV',Toon_A_checker+'.uvCoord')
		cmds.connectAttr(Toon_A_place2dTexture+'.outUvFilterSize',Toon_A_checker+'.uvFilterSize')
		cmds.connectAttr(Toon_A_checker+'.outColor',Toon_A_Dif+'.color')
		cmds.connectAttr(Toon_A_Spc+'.outColor',Toon_A_layered+'.inputs[0].color')
		cmds.connectAttr(Toon_A_Dif+'.outColor',Toon_A_layered+'.inputs[1].color')
		cmds.setAttr(Toon_A_layered+'.inputs[0].transparency' , 1, 1, 1, type = 'double3')
		cmds.setAttr(Toon_A_layered+'.inputs[1].transparency' , 1, 1, 1, type = 'double3')
	
		cmds.setAttr(Toon_A_ramp+'.colorEntryList[1].position',0.595)
		cmds.connectAttr(Toon_A_layered+'.outColor',Toon_A_ramp+'.colorEntryList[1].color')
		cmds.connectAttr(Toon_A_ramp+'.outColor',Toon_A_shd+'.color')
		
			
		#B
		Toon_B_shd = cmds.shadingNode('aiUtility', n = 'Toon_B' , asShader=True)
		cmds.setAttr(Toon_B_shd+'.shadeMode',2)
	
		Toon_B_ramp = cmds.shadingNode('ramp', n = 'ToonBRamp' , asTexture=True)
		cmds.setAttr(Toon_B_ramp+'.interpolation',0)
		cmds.removeMultiInstance(Toon_B_ramp+'.colorEntryList[2]' , b=1 )
		cmds.setAttr(Toon_B_ramp+'.colorEntryList[0].color',1,1,1, type = 'double3')
	
		Toon_B_samplerInfo = cmds.shadingNode('samplerInfo', n = 'ToonB_samplerInfo' , asUtility = True)
		cmds.connectAttr(Toon_B_samplerInfo+'.facingRatio',Toon_B_ramp+'.uCoord')
		cmds.connectAttr(Toon_B_samplerInfo+'.facingRatio',Toon_B_ramp+'.vCoord')
	
	
		Toon_B_Ami = cmds.shadingNode('aiStandard', n = 'Toon_BAmi' , asShader=True)
		cmds.setAttr(Toon_B_Ami+'.color',1,1,1, type = 'double3')
		cmds.setAttr(Toon_B_Ami+'.Kd',1)
		cmds.setAttr(Toon_B_Ami+'.specularRoughness',0)
		cmds.setAttr(Toon_B_Ami+'.directDiffuse', 20)
		cmds.setAttr(Toon_B_Ami+'.indirectDiffuse',0)
	
		cmds.setAttr(Toon_B_ramp+'.colorEntryList[1].position',0.595)
		cmds.connectAttr(Toon_B_Ami+'.outColor',Toon_B_ramp+'.colorEntryList[1].color')
		cmds.connectAttr(Toon_B_ramp+'.outColor',Toon_B_shd+'.color')
	
	#Ocean 만들기
	def Ocen_Edit(self, *args):
		appPath = __file__.replace("\\", "/")
		rootPath = appPath.rpartition("/")[0]
		texturesPath = rootPath + '/Textures'

	#Ocen_쉐이더 ( 오션쉐이더는 디퓨즈가없기때문에 쉐이더의 spc 부분에서 밝기를 조절하여야한다.
	#쉐이더만들기
		Ocean_shd = cmds.shadingNode('aiStandard', n = 'Ocean' , asShader=True)
		print 'Ocean Shader Created'
		cmds.setAttr(Ocean_shd+'.Kd',0)
		cmds.setAttr(Ocean_shd+'.Ks',1)
		cmds.setAttr(Ocean_shd+'.specularRoughness',0)
		cmds.setAttr(Ocean_shd+'.specularFresnel',1)
		cmds.setAttr(Ocean_shd+'.Ksn',0.2)
		cmds.setAttr(Ocean_shd+'.Kt',1)
		cmds.setAttr(Ocean_shd+'.IOR',1.33)
	#텍스쳐
		Ocean_vector_displacement = cmds.createNode('file',n='OceanVectorDisplacement')
		print 'Ocean Vector Displacement Created'
		Ocean_place2dTexture = cmds.shadingNode('place2dTexture', n = 'Ocean2dTexture' , asUtility = True)
		cmds.connectAttr(Ocean_place2dTexture+'.outUV',Ocean_vector_displacement+'.uvCoord')
		cmds.connectAttr(Ocean_place2dTexture+'.outUvFilterSize',Ocean_vector_displacement+'.uvFilterSize')
		cmds.setAttr(Ocean_vector_displacement+'.fileTextureName',texturesPath +'/vector-displacement_sea.exr', type = 'string' )
	
	
	
	#플랜+라이트만들기
		OcenPlane = cmds.polyPlane(n = 'OcenPlane')
		print 'Ocen Plane Created'
		cmds.scale( 600, 600, 600, OcenPlane, pivot=(0, 0, 0), absolute=True )
		OcenPlaneShape =  cmds.pickWalk(d='down')[0]
		print OcenPlaneShape

		cmds.setAttr(OcenPlaneShape+'.aiSubdivType',1)
		cmds.setAttr(OcenPlaneShape+'.aiSubdivIterations',7)
		cmds.setAttr(OcenPlaneShape+'.aiDispHeight',0.1)
		cmds.setAttr(OcenPlaneShape+'.aiDispPadding',1)
		cmds.setAttr(OcenPlaneShape+'.aiOpaque',0)
	
	#플랜과 쉐이더 연결하기
		cmds.select(OcenPlaneShape)
		cmds.hyperShade( assign = Ocean_shd)
		print 'Assign Ocean Shader'
	
	#디스맵
		Ocean_Disp = cmds.shadingNode('displacementShader',n='OceanDisp', asShader=True )
		cmds.setAttr(Ocean_Disp+'.scale',2)
		cmds.setAttr(Ocean_Disp+'.vectorSpace',0)
	#디스플레이에 연결되어있는 SG이름추출하기
		L = cmds.select(Ocean_shd) #쉐이더잡는다
		LL = cmds.ls(s=1) #잡은쉐이더 리스트추출한다.
		print LL
		LLL = cmds.listHistory( LL, future=True ) #선택된 쉐이더의 모든 히스토리리스트를 추출한다.
		LLLL = cmds.ls( type= 'shadingEngine')
		print LLLL[0]
	#디스백터에 디스백터맵 연결
		cmds.connectAttr(Ocean_vector_displacement+'.outColor' , Ocean_Disp+'.vectorDisplacement')
	# SG 에디스맵연결
		cmds.connectAttr(Ocean_Disp+'.displacement' , LLLL[0]+'.displacementShader')
	
	
	#Ocean Light
		OceanHdir = cmds.createNode('aiSky')
		print "Ocean Hdir : " + OceanHdir
		hdr = cmds.createNode('file',n='Oceanhdr')
		cmds.setAttr(hdr+'.fileTextureName',texturesPath +'/sky.hdr', type = 'string' )
		cmds.setAttr(hdr+'.colorGain',0.4,0.4,0.4, type = 'double3' )
		cmds.connectAttr(hdr+'.outColor', OceanHdir+'.color')
	#아놀드에서 트렌스폼 연결하는것이다 이것은 감춰져있기떄문에 찾기어려우나,sky 를잡고 연결을파악한후 연결하면된다.
		cmds.connectAttr(OceanHdir+'.message','defaultArnoldRenderOptions.background')
	
	#디렉션 스펙뮬러
		Oceanlight = cmds.directionalLight(rotation=(0, 60, 60))
		cmds.setAttr(Oceanlight+'.aiAngle',6)
		cmds.setAttr(Oceanlight+'.aiAngle',6)
		cmds.setAttr(Oceanlight+'.aiCastShadows',0)
		cmds.setAttr(Oceanlight+'.emitDiffuse',0)
	
	
	#r쉐이더
	def R_shd_Edit(self, *args):
		R_shd = cmds.shadingNode('aiUtility', n = 'RShd' , asShader=True)
		cmds.setAttr(R_shd+'.shadeMode',2)
		R_aiUserDataColor = cmds.shadingNode('aiUserDataColor', n = 'RDataColor' , asUtility=True)
		cmds.setAttr(R_aiUserDataColor+'.defaultValue' , 1,0,0, type = 'double3')
		cmds.connectAttr(R_aiUserDataColor+'.outColor',R_shd+'.color')
	#g쉐이더
	def G_shd_Edit(self, *args):
		G_shd = cmds.shadingNode('aiUtility', n = 'GShd' , asShader=True)
		cmds.setAttr(G_shd+'.shadeMode',2)
		G_aiUserDataColor = cmds.shadingNode('aiUserDataColor', n = 'GDataColor' , asUtility=True)
		cmds.setAttr(G_aiUserDataColor+'.defaultValue' , 0,1,0, type = 'double3')
		cmds.connectAttr(G_aiUserDataColor+'.outColor',G_shd+'.color')
	#b쉐이더
	def B_shd_Edit(self, *args):
		B_shd = cmds.shadingNode('aiUtility', n = 'BShd' , asShader=True)
		cmds.setAttr(B_shd+'.shadeMode',2)
		B_aiUserDataColor = cmds.shadingNode('aiUserDataColor', n = 'BDataColor' , asUtility=True)
		cmds.setAttr(B_aiUserDataColor+'.defaultValue' , 0,0,1, type = 'double3')
		cmds.connectAttr(B_aiUserDataColor+'.outColor',B_shd+'.color')


























































