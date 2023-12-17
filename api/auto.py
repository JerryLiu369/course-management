class MC(db.Model):
    Mname = db.Column(db.String(255), primary_key=True)
    Cname = db.Column(db.String(255), primary_key=True)
    MCcategory = db.Column(db.String(255))
    MCmodules = db.Column(db.String(255))

# 获取数据库中的 MC 表数据
def get_mc_data():
    mc_data = MC.query.all()
    return mc_data

# 根据数据库中的数据构建新的 ALLMODULES 结构
def update_all_modules(mc_data):
    new_all_modules = []

    for row in mc_data:
        mname = row.Mname
        cname = row.Cname
        category = row.MCcategory
        module = row.MCmodules

        # 在 new_all_modules 中找到对应的模块，如果不存在则添加
        module_found = False
        for module_data in new_all_modules:
            if module_data['name'] == mname:
                for category_data in module_data['categories']:
                    if category_data['name'] == category:
                        if module not in category_data['modules']:
                            category_data['modules'].append(module)
                        module_found = True
                        break
                break

        if not module_found:
            new_module_data = {
                'name': mname,
                'categories': [
                    {'name': category, 'modules': [module]}
                ]
            }
            new_all_modules.append(new_module_data)

    return new_all_modules