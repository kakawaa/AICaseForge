class PromptConfig:
    # 注入知识,根据文档生成faq问答对
    FAQ = """
如下三个反引号中是"{product}"产品文档的相关知识信息
```
{page}
```
如下三个反引号中是从知识信息中提取的关键词列表
```
{keywords}
```
请仔细阅读以上知识信息和关键词列表，基于知识信息、关键词列表自动生成{nums}个独立的问题以及对应答案, 要求尽可能详细全面, 并且遵循如下规则:
1. 问题需要详细全面地覆盖知识信息的内容，同时关键词或"{product}"需要被恰当地包含在Question中
2. 生成的内容不要超出反引号的信息范围
3. 问题部分需要以"Question:"开始，答案部分需要以"Answer:"开始
4. 若产品文档片段内容过少，知识信息不足以回答问题，答案部分为空，即只保留"Answer:"
5. 总共生成{nums}个问答对
6. put your output between <output> and </output>，每个问题和答案作为一个独立的段落。每个段落以一个空行分隔。输出示例为
<output>
Question: "应答流程-ASR处理单元"的单元配置包括哪些内容？
Answer: 用户的输入内容完全匹配噪音词的内容，则认为是噪音；词表模板为excel文件，表头为：噪音词（只解析第一列，每行一个值）。噪音目前的判断逻辑为：识别内容长度小于2并且得分小于0.5；该逻辑从维度上和后续的业务发展情况看较为定制，建议底层写死，不开放配置。

Question: "应答流程-反问处理单元"是什么？
Answer: "应答流程-反问处理单元"是主要用于在无法直接应答的情况下触发反问及拼装处理的单元。它处理反问节点的触发，以及反问回收情况的拼接。该单元配置中目前仅开放实体反问举例及二次，不开放意图反问举例和二次，意图反问话术只支持固定话术配置。该单元还涉及到反问类型的分类，会话内反问次数的限制，以及反问的优先级处理。
</output>
"""

    # 根据召回文本生成测试用例
    GEN_CASE_BY_RECALL = """
你作为系统测试专家，精通测试用例的设计。请根据以上的产品需求文档和技术设计文档,输出编写测试用例。
规则:
1. 要求将测试步骤及预期结果细化到各个字段,以{case_type}格式输出测试用例
2. 不要输出性能、安全测试用例，尽量输出功能测试用例
3. 不要输出不符合逻辑的特殊测试用例，如未知操作产生的不定结果
4. 详细阅读和理解产品需求文档和技术设计文档，确定测试的关键点和可能的风险点
5. 将测试步骤及预期结果细化到各个字段,当产品需求文档与技术设计文档重合度不高时,以产品需求文档为准
6. 输出内容字数不要超过800
7. put your output between <output> and </output>
用例模版是
"""

    # 根据需求文档生成测试用例
    GEN_CASE_BY_REQ_SYS = "你是一位资深的软件测试工程师，专注于编写详细且全面的功能测试用例。你的任务是根据需求文档分析关键信息，设计出覆盖所有功能点、边界条件、等价类的测试用例以验证软件的功能。"
    GEN_CASE_BY_REQ = """
任务：请根据原需求文档、和你输出的优化后的markdown需求文档，编写详细的功能测试用例。请确保你的测试用例遵循以下格式和指导原则：

使用{case_type}格式生成测试用例，用例模板为：
{empty_case}

要求：
1. 仔细阅读并理解产品需求文档，以确定测试的关键点和潜在风险点。
2. 测试用例需详细到每个字段，包括测试步骤和预期结果，并使用上述{case_type}格式记录。
3. 确保测试用例全面覆盖所有功能点、边界条件、等价类、状态变化和输入组合。
4. 特别注意验证所有富文本样式的正确显示与功能，包括但不限于字体样式（加粗、下划线、倾斜）、字体颜色（确保符合标准色值）、背景色、字体大小、超链接（特别是对短链的兼容性）、以及富文本中的按钮、表格、图片等元素。
5. 对于必填和非必填字段，明确指出并设计相应的测试用例，确保测试用例覆盖这两类字段的验证。
6. 仅需编写功能测试用例，不包括性能和安全测试。
7. 忽略逻辑不合理或结果不确定的特殊测试用例。
8. 必须保留所有关键信息，包括判断条件和具体数值，包含对大小、尺寸、字段、枚举值等具体数值的测试。
{human_input}
测试用例设计方法：
- **等价类划分**：为每个必填字段设计测试用例，验证字段为空时系统的响应。对于非必填字段，验证为空时系统的处理能力。
- **边界值分析**：对于有特定输入范围的字段，测试边界值（最小值、最小值-1、最大值、最大值+1）以确保系统正确处理边界情况。
- **错误猜测**：基于常见错误模式，设计测试用例来验证系统对错误操作的响应。
- **状态测试**：对不同用户状态（如新用户、返回用户、已验证用户等）的表单或应用程序，确保测试用例覆盖不同状态下的必填和非必填条件。
- **决策表测试**：使用决策表来验证不同条件组合下的系统行为。
- **配对测试**：选择两个或更多的输入字段，测试它们的所有可能组合。

请在完成任务后，将你的输出放在<output>和</output>标签之间，注意，你的输出应只包含{case_type}数据。
"""

    # 需求文档改写
    REWRITE_DOC_SYS = "你是一位经验丰富的金融客服系统测试专家,专注于设计和执行测试用例以确保软件产品满足其规定的需求和标准。你具备深厚的理解能力,能够快速把握产品需求文档的关键信息,并将其转化为详细的测试计划"
    REWRITE_DOC = """
## 技能
### 技能1: 需求文档分析
- 仔细阅读并分析提供的产品需求文档。
- 识别文档中的关键功能和性能要求。
- 确保理解所有功能点和边界条件。

### 技能2: 测试用例设计
- 使用等价类划分、边界值分析、错误猜测、状态猜测等方法设计测试用例。
- 确保测试用例覆盖所有判断条件，如“字段是否必填”“能否跳转”等。
- 包含对大小、尺寸、字段、枚举值等具体数值的测试。

### 技能3: 文档优化
- 基于对需求的深入理解，优化原始需求文档。
- 保留关键信息，如判断条件和具体数值。
- 提高文档的可读性和可操作性。

## 约束
- 在优化文档时，必须保留所有关键信息，包括判断条件和具体数值。
- 优化后的文档应更加清晰，易于理解和执行测试。
- 使用Markdown格式输出。

## 任务清单
1. 仔细阅读并分析"{product}"的需求文档
2. 识别并记录所有关键功能点和性能要求，覆盖所有功能点和边界条件。
3. 优化需求文档，保留所有关键信息，并提高其可读性。
4. 使用Markdown格式整理并输出优化后的需求文档。 尽力保留所有信息（文本、格式、流程图、图表）。将表格转换为 Markdown 表格格式

如下三个反引号中是需求文档"{product}"的内容
```
{content}
```
"""

    SUMMARY = "作为软件测试开发专家，请根据以下的产品设计文档,输出总结，总结字数不要超过40字。注意，你输出的总结将作为知识库插入到向量数据库中，为了提升语义检索的精准度，你提供的总结必须要非常精准: \n{input_text}\n"

    # 对一整页进行理解分析
    PAGE_ANALYSIS = """
下面三个反引号中是需求文档的内容，你需要根据需求文档进行图片的详细描述
```
{content}
```
1. 根据图像中的布局，确定输出顺序。 如果没有明确的顺序，则先转换文本部分，然后转换图表部分。
2. 以Markdown格式输出。 尽力保留所有信息（文本、格式、流程图、图表）。
3. 注意格式，保持引用和标题的水平。
4. 将表格转换为 Markdown 表格格式
5. 将条形图转换为项目符号格式，使用 Chart Title 作为标题， 类别标签作为项目符号标题，值标签作为值，保留所有类别标签。
6. 将饼图转换为项目符号格式，使用图表标题作为标题，类别标签作为项目符号标题，值标签作为值，保留所有类别标签。
7. 将流程图、时序图转换为Mermaid对应的code，保留所有类别标签。
8. 图片与原文语言一致。将输出放在 <output> 和 </output> 之间
"""

    # 对单张图片进行理解分析
    IMG_ANALYSIS = """
你需要进行图片的详细描述，要求如下
1. 以Markdown格式输出。 尽力保留所有信息（文本、格式、流程图、图表）。若你需要输出Markdown格式的标题，请将标题转换为正文形式输出。
2. 注意格式，保持引用和标题的水平。
3. 将表格转换为 Markdown 表格格式
4. 将条形图转换为项目符号格式，使用 Chart Title 作为标题， 类别标签作为项目符号标题，值标签作为值，保留所有类别标签。
5. 将饼图转换为项目符号格式，使用图表标题作为标题，类别标签作为项目符号标题，值标签作为值，保留所有类别标签。
6. 将流程图、时序图转换为Mermaid对应的code，保留所有类别标签。
7. 图片与原文语言一致,将输出放在 <output> 和 </output> 之间。
"""

    # 转换xmind测试用例case
    XMIND_ANALYSIS = """
 下面三个反引号中是xmind文件中测试用例的内容，你需要根据语义对测试用例进行重写
```
{content}
```   
使用json格式转换测试用例，用例模板为：
{empty_case}

要求：
1. 仔细阅读并理解json结构，以保障后续转换测试用例语义的流畅性。
2. 测试用例需详细到每个字段，包括测试步骤和预期结果，并使用json格式记录。
3. 确保覆盖所有原测试用例内容
4. json中的每一级都可能是测试用例，请不要有遗漏
"""