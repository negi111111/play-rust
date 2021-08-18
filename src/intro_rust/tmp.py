    # ---------- dashboard ----------
    path(  # GET: キャンバスのメタ情報取得
        "projects/<int:proj_id>/canvas/<int:canvas_id>/meta",
        dashboard_views.CanvasInfoView.as_view(),
        name="project_info_view",
    ),
    path(  # GET: モジュール一覧および設置済みカード一覧取得
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards",
        dashboard_views.ProjectCardsView.as_view(),
        name="project_cards",
    ),
    path(  # GET: 実験管理の結果データ取得
        "projects/<int:proj_id>/canvas/<int:canvas_id>/experiments",
        dashboard_views.ExperimentalResultView.as_view(),
        name="experimental_result",
    ),
    # データツール
    path(  # POST: ローカルファイルのupload
        "projects/upload/<int:proj_id>",
        data_views.FileUploadView.as_view(),
        name="pjfileupload",
    ),
    path(  # POST: クラウド上のファイルのupload
        "projects/cloud_storage_upload/<int:proj_id>",
        data_views.CloudStorageFileUploadView.as_view(),
        name="pjcloudstoragefileupload",
    ),
    path(  # POST: アップロード済みCSVファイルのfth変換
        "projects/<int:proj_id>/fileconvert/<slug:item_id>/start",
        data_views.StartFileConvertView.as_view(),
        name="stop_file_convert",
    ),
    path(  # POST: CSVファイルのfth変換中止
        "projects/<int:proj_id>/fileconvert/<slug:item_id>/stop",
        data_views.StopFileConvertView.as_view(),
        name="stop_file_convert",
    ),
    path(  # GET: CSVファイル変換状況確認
        "projects/<int:proj_id>/fileconvert/<slug:item_id>/check",
        data_views.CheckFileConvertView.as_view(),
        name="check_file_convert",
    ),
    path(  # GET: プロジェクトで使用可能なpublicなアップロード済みファイル一覧取得
        "public_files_json",
        data_views.PublicFilesJsonView.as_view(),
        name="public_files_json",
    ),
    path(  # GET: プロジェクトで使用可能なprivateなアップロード済みファイル一覧取得
        "projects/files_json/<int:proj_id>",
        data_views.ListFilesJsonView.as_view(),
        name="listpjfilesjson",
    ),
    path(  # DELETE: アップロード済みファイルを削除
        "projects/<int:proj_id>/delete_uploaded_file",
        data_views.DeleteUploadedFileView.as_view(),
        name="delete_uploaded_file",
    ),
    path(  # POST: カードをダッシュボード上に設置
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/create",
        dashboard_views.CreateCardView.as_view(),
        name="createcard",
    ),
    path(  # POST: テキストカードをダッシュボード上に設置
        "projects/<int:proj_id>/canvas/<int:canvas_id>/text_cards/create",
        dashboard_views.CreateTextCardView.as_view(),
        name="createtextcard",
    ),
    path(  # PUT: カードの位置を更新
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/update",
        dashboard_views.UpdateCardView.as_view(),
        name="updatecard",
    ),
    path(  # PUT: カードの表示名を更新
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/update_name",
        dashboard_views.UpdateCardNameView.as_view(),
        name="updatecardname",
    ),
    path(  # PUT: テキストカードの位置を更新
        "projects/<int:proj_id>/canvas/<int:canvas_id>/text_cards/<slug:text_card_id>/update",
        dashboard_views.UpdateTextCardView.as_view(),
        name="updatetextcard",
    ),
    path(  # DELETE: カードを削除する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/delete",
        dashboard_views.DeleteCardView.as_view(),
        name="delete_card",
    ),
    path(  # DELETE: テキストカードを削除する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/text_cards/<slug:text_card_id>/delete",
        dashboard_views.DeleteTextCardView.as_view(),
        name="deletetextcard",
    ),
    path(  # POST: カードを複数削除する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/bulk_delete",
        dashboard_views.BulkDeleteCardView.as_view(),
        name="bulk_delete_cards",
    ),
    path(  # POST: テキストカードを複数削除する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/text_cards/bulk_delete",
        dashboard_views.BulkDeleteTextCardView.as_view(),
        name="bulk_delete_textcards",
    ),
    path(  # POST: カードをコピーする
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/copy",
        dashboard_views.CopyCardView.as_view(),
        name="copy_card",
    ),
    path(  # POST: テキストカードをコピーする
        "projects/<int:proj_id>/canvas/<int:canvas_id>/text_cards/<slug:text_card_id>/copy",
        dashboard_views.CopyTextCardView.as_view(),
        name="copy_textcard",
    ),
    path(  # POST: カードを複数コピーする
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/bulk_copy",
        dashboard_views.BulkCopyCardView.as_view(),
        name="bulk_copy_cards",
    ),
    path(  # POST: テキストカードを複数コピーする
        "projects/<int:proj_id>/canvas/<int:canvas_id>/text_cards/bulk_copy",
        dashboard_views.BulkCopyTextCardView.as_view(),
        name="bulk_copy_textcards",
    ),
    path(  # POST: カード実行
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/execute",
        dashboard_views.ExecuteCardView.as_view(),
        name="executecard",
    ),
    path(  # GET: モデルをローカル環境にダウンロードする
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/exportmodel_to_local",
        dashboard_views.ExportModelToLocalView.as_view(),
        name="exportmodel_to_local",
    ),
    path(  # GET: モデルをクラウドストレージにアップロードする
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/exportmodel_to_cloud_storage",
        dashboard_views.ExportModelToCloudStorageView.as_view(),
        name="exportmodel_to_cloud_storage",
    ),
    path(  # GET: 出力データをローカルにダウンロードする
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/download_output",
        dashboard_views.DownloadOutputView.as_view(),
        name="download_output",
    ),
    path(  # POST: テキストカード内のテキストを保存する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/text_cards/<slug:text_card_id>/save_text",
        dashboard_views.SaveTextView.as_view(),
        name="savetext",
    ),
    # メモ
    path(  # POST: コメントの作成
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/create_comment",
        dashboard_views.CreateCommentView.as_view(),
        name="create_comment",
    ),
    path(  # GET: コメント内容の取得
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/load_comment",
        dashboard_views.LoadCommentView.as_view(),
        name="load_comment",
    ),
    path(  # PUT: コメント内容の更新
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/update_comment",
        dashboard_views.UpdateCommentView.as_view(),
        name="update_comment",
    ),
    path(  # DELETE: コメント内容の削除
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/delete_comment",
        dashboard_views.DeleteCommentView.as_view(),
        name="delete_comment",
    ),
    path(  # DELETE: コメントスレッドの削除
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/delete_thread",
        dashboard_views.DeleteCommentThreadView.as_view(),
        name="delete_comment",
    ),
    # 学習処理
    path(  # GET: 学習の途中描画情報を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/trainprogress",
        dashboard_views.TrainProgressView.as_view(),
        name="trainprogress",
    ),
    path(  # GET: 線形学習の途中描画情報を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/linear_trainprogress",
        dashboard_views.LinearTrainProgressView.as_view(),
        name="linear_trainprogress",
    ),
    path(  # GET: パラメータ探索結果を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/validation_result",
        dashboard_views.ValidationResultView.as_view(),
        name="validation_result",
    ),
    path(  # GET: 探索で用いたモデル構成を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/hpsearch/params_view/<slug:search_id>",
        dashboard_views.HpsearchParamsView.as_view(),
        name="hpsearch_paramsview",
    ),
    path(  # POST: 学習を停止させる
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/trainstop",
        dashboard_views.TrainAbortView.as_view(),
        name="trainstop",
    ),
    path(  # POST: ハイパラ自動探索を中止する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/quitsearch",
        dashboard_views.QuitSearchView.as_view(),
        name="quitsearch",
    ),
    # カード詳細画面
    path(  # GET: カードコンフィグを取得
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/view",
        dashboard_views.CardContentView.as_view(),
        name="cardcontent",
    ),
    path(  # GET: 俯瞰グラフの分割点情報取得
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/graphsplitpoint",
        dashboard_views.GraphSplitPointView.as_view(),
        name="splitpoint",
    ),
    path(  # GET: グラフのカラム情報を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/graphmetadata",
        dashboard_views.GraphMetadataView.as_view(),
        name="graphmeta",
    ),
    path(  # GET: グラフ情報を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/graphdata",
        dashboard_views.GraphDataView.as_view(),
        name="graphdata",
    ),
    path(  # GET: テーブル情報を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/data/<slug:pagenum>",
        dashboard_views.TableView.as_view(),
        name="tableview",
    ),
    path(  # GET: データの統計情報を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/stats",
        dashboard_views.StatsView.as_view(),
        name="statsview",
    ),
    path(  # GET: Evaluateの評価指標値を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/evaluatemetadata",
        dashboard_views.EvaluateMetadataView.as_view(),
        name="evaluatemeta",
    ),
    path(  # GET: 要因分析のコンテンツを返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/attribution",
        dashboard_views.AttributionView.as_view(),
        name="attribution",
    ),
    path(  # GET: 因果分析のテーブルデータを返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/causal_table",
        dashboard_views.CausalTableView.as_view(),
        name="causal_table",
    ),
    path(  # GET: 因果分析のグラフデータを返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/causal_graph",
        dashboard_views.CausalGraphView.as_view(),
        name="causal_graph",
    ),
    path(  # GET: ConcatTimeSeriesWindow のリストを返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/concat_time-series_window",
        dashboard_views.ConcatTimeSeriesWindowView.as_view(),
        name="concat_time-series_window",
    ),
    path(  # GET: Trainingの学習結果を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/train",
        dashboard_views.TrainView.as_view(),
        name="trainview",
    ),
    path(  # GET: MLPのレイヤー構造を返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/modelview",
        dashboard_views.ModelView.as_view(),
        name="modelview",
    ),
    path(  # GET: 再現誤差の超過カウントを返す
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/reconstruction_error_count",
        dashboard_views.ReconstructionErrorCountView.as_view(),
        name="reconstruction_error_count",
    ),
    path(  # POST: 描画に関するデータを保存する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/save_drawparam",
        dashboard_views.SaveDrawParamView.as_view(),
        name="save_draw_param",
    ),
    path(  # GET: 描画に関するデータを取得する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/cards/<slug:card_id>/drawparam",
        dashboard_views.DrawParamView.as_view(),
        name="draw_param",
    ),
    # 接続
    path(  # POST: execute linkの結線
        "projects/<int:proj_id>/canvas/<int:canvas_id>/connect",
        dashboard_views.ConnectCardView.as_view(),
        name="connect",
    ),
    path(  # POST config linkの結線
        "projects/<int:proj_id>/canvas/<int:canvas_id>/connect_link",
        dashboard_views.ConnectLinkView.as_view(),
        name="connect_link",
    ),
    path(  # DELETE: execute linkの削除
        "projects/<int:proj_id>/canvas/<int:canvas_id>/delete_connect",
        dashboard_views.DeleteConnectView.as_view(),
        name="delete_connect",
    ),
    path(  # DELETE: config linkの削除
        "projects/<int:proj_id>/canvas/<int:canvas_id>/delete_link",
        dashboard_views.DeleteConfigLinkView.as_view(),
        name="delete_link",
    ),
    # レシピ
    path(  # GET: projectのレシピ一覧を取得する
        "projects/<int:proj_id>/recipes/recipe_list",
        recipe_views.ListRecipeView.as_view(),
        name="list_recipe"
    ),
    path(  # POST: projectのレシピを読み込む
        "projects/<int:proj_id>/canvas/<int:canvas_id>/import_recipe",
        recipe_views.ImportRecipeView.as_view(),
        name="import_recipe",
    ),
    path(  # POST: canvasのテンプレートを保存する
        "projects/<int:proj_id>/canvas/<int:canvas_id>/export_recipe",
        recipe_views.ExportRecipeView.as_view(),
        name="export_recipe",
    ),
    path(  # DELETE: レシピ削除
        "recipes/<int:recipe_id>/delete",
        recipe_views.DeleteRecipeView.as_view(),
        name="delete_recipe",
    ),
    path(  # GET: メールアドレス取得
        "users/config/notification",
        user_views.GetUserNotificationView.as_view(),
        name="get_notification",
    ),
    path(  # POST: メールアドレス登録
        "users/config/notification/save",
        user_views.UserNotificationView.as_view(),
        name="save_notification",
    ),