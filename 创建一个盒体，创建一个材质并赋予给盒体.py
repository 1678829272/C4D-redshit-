import c4d

def main():


    # 创建一个盒体对象
    cube = c4d.BaseObject(c4d.Ocube)
    cube.SetAbsPos(c4d.Vector(0, 0, 0))  # 设置盒体位置
    cube.SetRelScale(c4d.Vector(100, 100, 100))  # 设置盒体尺寸
    doc.InsertObject(cube) #把盒体添加到场景中
    mat_tag = c4d.BaseTag(c4d.Ttexture) #创建一个材质标签对象
    mat = c4d.BaseMaterial(c4d.Mmaterial)#创建一个材质对象
    mat[c4d.MATERIAL_COLOR_COLOR]=c4d.Vector(1, 0, 0) #设置材质的基础颜色为红色
    doc.InsertMaterial(mat)#把材质添加到场景中
    
    mat_tag[c4d.TEXTURETAG_MATERIAL]=mat#把材质对象赋予给材质标签
    cube.InsertTag(mat_tag)#把材质标签赋予给盒体  

    # 更新文档
    c4d.EventAdd()


if __name__=='__main__':
    main()