---
title: "Yii使用model进行设置查询规则/模型/控制器"
date: "2025-06-05 10:52:51"
slug: "yii-shi-yong-model-jin-xing-she-zhi-cha-xun-gui-ze-mo-xing-kong-zhi-qi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/05/Yii使用model进行设置查询规则/模型/控制器/"
  - "/2025/06/05/Yii使用model进行设置查询规则/模型/控制器.html"
  - "/Yii使用model进行设置查询规则/模型/控制器/"
  - "/Yii使用model进行设置查询规则/模型/控制器.html"
  - "/2025/06/05/Yii使用model进行设置查询规则-模型-控制器/"
  - "/2025/06/05/Yii使用model进行设置查询规则-模型-控制器.html"
  - "/2025/06/05/yii-shi-yong-model-jin-xing-she-zhi-cha-xun-gui-ze-mo-xing-kong-zhi-qi/"
  - "/2025/06/05/yii-shi-yong-model-jin-xing-she-zhi-cha-xun-gui-ze-mo-xing-kong-zhi-qi.html"
  - "/yii-shi-yong-model-jin-xing-she-zhi-cha-xun-gui-ze-mo-xing-kong-zhi-qi.html"
---
yii有个查询数据的便利的地方，就是可以在model层设置查询规则，然后在controller层，直接调用，进行数据查询：

举个例子说明一下：

先从model层说起：model名称叫做Blog，继承自CActiveRecord

```php
function scopes()
{
    return [
        'published' => [
            'condition' => 'status=1',
        ],
        'recently' => [
            'order' => 'create_date DESC',
            'limit' => 5,
        ],
        'createDateDesc' => [
            'order' => 'create_date DESC',
        ],
    ];
}
```

在上面的代码中，继承函数scopes,然后在里面命名自己想要使用的规则名称。

我这里使用了

published，recently，createCateDesc，分别对应sql语句的一部分，这个在调用controller的时候会合并到总的sql语句里面去的。

下面看在controller里面怎么使用

```php
//最近的博文
$rawData = Blog::model()->recently()->findAll();
$rawData = new CArrayDataProvider($rawData, [
    'sort' => [
        'attributes' => [
            'id',
            'title',
        ],
    ],
    'pagination' => [
        'pageSize' => 10,
    ],
]);
```
我在自己的BlogController控制器，action为actionView的方法中引用了这样一个代码：

注意其中的recently部分

```php
$rawData=Blog::model()->recently()->findAll();
```

这个就是我们在model层设置的规则，在这里作为方法被调用了。

是不是很方便呀。

详细的代码我贴到下面：

```php model

<?php

/**
 * This is the model class for table "tbl_blog".
 *
 * The followings are the available columns in table 'tbl_blog':
 * @property integer $id
 * @property string $title
 * @property string $description
 * @property string $create_date
 * @property string $update_date
 */
class Blog extends CActiveRecord
{
    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return Blog the static model class
     */
    public static function model($className = __CLASS__)
    {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName()
    {
        return 'tbl_blog';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules()
    {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return [
            ['title', 'required', 'message' => '标题不能为空'],
            ['description', 'required', 'message' => '内容不能为空'],
            ['title', 'length', 'max' => 255],
            ['tag', 'safe'],
            ['type_id', 'safe'],
            ['update_date', 'safe'],
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            ['id, title, description, create_date, update_date', 'safe', 'on' => 'search'],
        ];
    }

    /**
     * @return array relational rules.
     */
    public function relations()
    {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return [
        ];
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels()
    {
        return [
            'id' => 'ID序号',
            'title' => '标题',
            'description' => '内容',
            'tag' => '标签(使用逗号进行分割)',
            'type_id' => '分类类型',
            'create_date' => '创建时间',
            'update_date' => '更新时间',
        ];
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search()
    {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria();

        $criteria->compare('id', $this->id);
        $criteria->compare('title', $this->title, true);
        $criteria->compare('description', $this->description, true);
        $criteria->compare('create_date', $this->create_date, true);
        $criteria->compare('update_date', $this->update_date, true);
        $criteria->scopes = 'createDateDesc';
        return new CActiveDataProvider($this, [
            'criteria' => $criteria,
        ]);
    }

    /**
     * 行为操作
     */
    public function behaviors()
    {
        return [
            'CTimestampBehavior' => [
                'class' => 'zii.behaviors.CTimestampBehavior',
                'createAttribute' => 'create_date',
                'updateAttribute' => 'update_date',
                'setUpdateOnCreate' => 'true',
            ],

        ];
    }

    //查询范围
    public function scopes()
    {
        return [
            'published' => [
                'condition' => 'status=1',
            ],
            'recently' => [
                'order' => 'create_date DESC',
                'limit' => 5,
            ],
            'createDateDesc' => [
                'order' => 'create_date DESC',
            ],
        ];
    }
}
```

```php controller

<?php
class BlogController extends Controller
{
    /**
     * @var string the default layout for the views. Defaults to '//layouts/column2', meaning
     * using two-column layout. See 'protected/views/layouts/column2.php'.
     */
    public $layout = '//layouts/column2';

    /**
     * @return array action filters
     */
    public function filters()
    {
        return [
            'accessControl', // perform access control for CRUD operations
            'postOnly + delete', // we only allow deletion via POST request
        ];
    }

    /**
     * Specifies the access control rules.
     * This method is used by the 'accessControl' filter.
     * @return array access control rules
     */
    public function accessRules()
    {
        return [
            ['allow', // allow all users to perform 'index' and 'view' actions
                'actions' => ['view'],
                'users' => ['*'],
            ],
            ['allow', // allow authenticated user to perform 'create' and 'update' actions
                'actions' => ['create', 'update', 'index'],
                'users' => ['@'],
            ],
            ['allow', // allow admin user to perform 'admin' and 'delete' actions
                'actions' => ['admin', 'delete'],
                'user' => ['admin'],
            ],
            ['deny', // deny all users
                'users' => ['*'],
            ],
        ];
    }

    /**
     * Displays a particular model.
     * @param integer $id the ID of the model to be displayed
     */
    public function actionView($id)
    {
        //最近的博文
        $rawData = Blog::model()->recently()->findAll();
        $rawData = new CArrayDataProvider($rawData, [
            'sort' => [
                'attributes' => [
                    'id',
                    'title',

                ],
            ],
            'pagination' => [
                'pageSize' => 10,
            ],
        ]);

        $recentBlogMenu = [];
        foreach ($rawData->getData() as $key => $value) {
            $recentBlogMenu[] = [
                'label' => $value->title,
                'url' => ['blog/view', 'id' => $value->id],
            ];
        }

        //博文的分类
        $rawData = Type::model()->findAll();
        $rawData = new CArrayDataProvider($rawData, [
            'sort' => [
                'attributes' => [
                    'id',
                    'name',
                ],
            ],
        ]);

        $blogType = [];
        foreach ($rawData->getData() as $key => $value) {
            $blogType[] = [
                'label' => $value->name,
                'url' => ['type/search/' . $value->id],
            ];
        }

        $this->render('view', [
            'model' => $this->loadModel($id),
            'blogType' => $blogType,
            'recentBlogMenu' => $recentBlogMenu,
        ]);
    }

    /**
     * Creates a new model.
     * If creation is successful, the browser will be redirected to the 'view' page.
     */
    public function actionCreate()
    {
        $model = new Blog;

        // Uncomment the following line if AJAX validation is needed
        // $this->performAjaxValidation($model);

        if (isset($_POST['Blog'])) {
            $model->attributes = $_POST['Blog'];
            if ($model->save()) {
                $this->redirect(['view', 'id' => $model->id]);
            }
        }

        $rawData = new CActiveDataProvider(
            'Type',
            [
                'sort' => [
                    'attributes' => [
                        'id',
                        'name',

                    ],
                ],
            ]
        );

        foreach ($rawData->getData() as $key => $value) {
            $type[$value->id] = $value->name;
        }

        $this->render('create', [
            'model' => $model,
            'type' => $type,
        ]);
    }

    /**
     * Updates a particular model.
     * If update is successful, the browser will be redirected to the 'view' page.
     * @param integer $id the ID of the model to be updated
     */
    public function actionUpdate($id)
    {
        $model = $this->loadModel($id);

        // Uncomment the following line if AJAX validation is needed
        // $this->performAjaxValidation($model);

        if (isset($_POST['Blog'])) {
            $model->attributes = $_POST['Blog'];
            if ($model->save()) {
                $this->redirect(['view', 'id' => $model->id]);
            }
        }

        $rawData = new CActiveDataProvider(
            'Type',
            [
                'sort' => [
                    'attributes' => [
                        'id',
                        'name',

                    ],
                ],
            ]
        );

        foreach ($rawData->getData() as $key => $value) {
            $type[$value->id] = $value->name;
        }

        $this->render('update', [
            'model' => $model,
            'type' => $type,
        ]);
    }

    /**
     * Deletes a particular model.
     * If deletion is successful, the browser will be redirected to the 'admin' page.
     * @param integer $id the ID of the model to be deleted
     */
    public function actionDelete($id)
    {
        $this->loadModel($id)->delete();

        // if AJAX request (triggered by deletion via admin grid view), we should not redirect the browser
        if (!isset($_GET['ajax'])) {
            $this->redirect(isset($_POST['returnUrl']) ? $_POST['returnUrl'] : ['admin']);
        }
    }

    /**
     * Lists all models.
     */
    public function actionIndex()
    {
        $dataProvider = new CActiveDataProvider(
            'Blog',
            [
                'pagination' => ['pageSize' => 10],
                'criteria' => [
                    'order' => 'create_date DESC',
                ],
            ]
        );

        $this->render('index', [
            'dataProvider' => $dataProvider,
        ]);
    }

    /**
     * Manages all models.
     */
    public function actionAdmin()
    {
        $model = new Blog('search');
        $model->unsetAttributes(); // clear any default values
        if (isset($_GET['Blog'])) {
            $model->attributes = $_GET['Blog'];
        }

        $this->render('admin', [
            'model' => $model,
        ]);
    }

    /**
     * Returns the data model based on the primary key given in the GET variable.
     * If the data model is not found, an HTTP exception will be raised.
     * @param integer the ID of the model to be loaded
     */
    public function loadModel($id)
    {
        $model = Blog::model()->findByPk($id);
        if (null === $model) {
            throw new CHttpException(404, '请求的页面不存在.');
        }

        return $model;
    }

    /**
     * Performs the AJAX validation.
     * @param CModel the model to be validated
     */
    protected function performAjaxValidation($model)
    {
        if (isset($_POST['ajax']) && 'blog-form' === $_POST['ajax']) {
            echo CActiveForm::validate($model);
            Yii::app()->end();
        }
    }
}
```
