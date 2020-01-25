# https://stackoverflow.com/questions/34303422/how-to-change-the-font-size-and-color-of-markdown-cell-in-ipython-py-2-7-noteb#answers-header
style_css = """
<style>
    @import url('https://fonts.googleapis.com/css?family=Raleway&display=swap');
    
    div.text_cell_render h1 { /* Main titles bigger, centered */
        font-size: 2.2em;
        line-height:1.4em;
        text-align:center;
        color: #00090d;
    }
    div.text_cell_render h2 { /*  Parts names nearer from text */
        font-size: 1.8em;
        color:#f2f2f2;;
        border-radius: 3px;
        background: #2b916a;
        padding: 15px;
        width: 99%;
        height: 2em;
    }
    div.text_cell_render h3 { /*  Parts names nearer from text */
        font-size: 1.5em;
        color:#f2f2f2;
        background: #1eb4a6;
        border-radius: 3px;
        padding: 15px;
        width: 99%;
        height: 2em;
    }
    div.text_cell_render h4 { /*  Parts names nearer from text */
        font-size: 1.2em;
        color: #008874;
        border-bottom: 1px solid #008874;
        padding: 20px;
        width: 99%;
        height: 2em;
    }
    div.text_cell_render h5 { /*  Parts names nearer from text */
        font-size: 1em;
        color: #0070b8;
        font-style: normal;
        border-bottom: 1px solid #0070b8;
        padding: 20px;
        width: 99%;
        height: 2em;
    }
    div.text_cell_render h6 { /*  Parts names nearer from text */
        font-size: 0.8em;
        color: #0082a3;
        font-style: normal;
    }
    
    /* Customize text cells */
    div.text_cell_render { 
        font-family: 'Raleway', sans-serif;
    }    
    
    p,li,span {
        color:#0f0f0f;
    }
    
    .rendered_html,.text_cell_render,.rendered_html {
        font-style: normal;
        margin-top: -0.3em;
        margin-bottom: -0.3em;
    }
    
    .link_background {
        color: #f2f2f2;
    }

    .box {
      border-radius: 3px;
      border: 2px solid #60b985;
      padding: 20px;
      width: 99%;
      height: 2em;
    }

    .key {
        color: #b31919;
        text-decoration: underline;
    }
    .highlight{
        color:#b31919;
        font-weight: bold;
    }
    .note{
        background-color: #d9f3d8;
    }
</style>
"""