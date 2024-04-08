import c4d
from c4d import gui                                 #C4D的弹窗API : gui.MessageDialog('Hello World!')
import redshift         #导入redshift库，前提是正确的安装了redshift渲染器


def main():
    mat_Actives=doc.GetActiveMaterials()#获取场景中激活的（选中的）所有材质
    for mat in mat_Actives:
        if mat.GetType()==1036224:#1036224 是RS材质的ID，GetType可以获得一个材质的类型对应的ID
            #mat1= doc.GetMaterials()[0]#获取文档中第一个材质
            mat_master=redshift.GetRSMaterialNodeMaster(mat)#根据获取到的材质得到材质的 NodeMaster| 类型为：c4d.modules.graphview.GvNodeMaster | 作用是：GvNodeMaster是存储GvNode的集合。
            #a=bc.CreateNode(bc.GetRoot(),c4d.ID_OPERATOR_MATERIAL)  # GetName()  GetType gas.GetOutPorts(

            shader_graph_root=mat_master.GetRoot()#获取根节点，也就是着色器里面的Shader Graph 群组，类型是GvNode

            RS_Main_Mat=shader_graph_root.GetDown().GetNext()# getdown 获取上一个节点（GvNode），GetNext获取下一个节点（GvNode），两个配合使用就可以获取到RS的材质节点
            #print(RS_Main_Mat[c4d.REDSHIFT_SHADER_MATERIAL_DIFFUSE_ROUGHNESS]) #c4d.REDSHIFT_SHADER_MATERIAL_DIFFUSE_ROUGHNESS 这段含义其实对应的是一个Int 代表RS材质基础颜色里面的粗糙度

            new_base_mat=c4d.BaseMaterial(c4d.Mmaterial)#创建一个C4D基础材质
            new_base_mat[c4d.MATERIAL_COLOR_COLOR]=c4d.Vector(1, 0, 0)#设置材质的基础颜色为红色， MATERIAL_COLOR_COLOR C4D基础材质的基础颜色对应的ID
            doc.InsertMaterial(new_base_mat)    #把创建的基础材质添加到场景文档中
            new_base_mat[c4d.MATERIAL_COLOR_COLOR]=RS_Main_Mat[c4d.REDSHIFT_SHADER_MATERIAL_DIFFUSE_COLOR]#把RS材质的基础颜色的值赋值给创建材质的基础颜色



    c4d.EventAdd()#更新场景，文档
if __name__=='__main__':
    main()