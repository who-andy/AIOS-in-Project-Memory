# PS Evaluator Skill v0.1.0

针对香港本科 Personal Statement 的**专业匹配型评估 Skill**，目前包含 HKU BBA Accounting and Finance、HKUST BSc Economics and Finance 两份官方资料来源明确的专业画像。

工作内容：通用质量评分（70 分）、专业匹配度评分（30 分）、同篇文书跨专业比较、两个版本盲评，以及多评委结果汇总和一致性诊断。

**适用边界**：这套权重是实验设计，并非香港高校官方评分标准。90 分和 80 分不对应可计算的录取概率。Skill 不会自动调用 Claude/GPT 的 API。语言模型负责作出有证据支持的定性判断，本地脚本负责校验、汇总与计算。

## 安装

将完整 `ps-evaluator` 文件夹复制至 Agent Skills 目录：

- Codex：`~/.agents/skills/ps-evaluator/`，或项目下 `.agents/skills/ps-evaluator/`。
- Claude Code：`~/.claude/skills/ps-evaluator/`，或项目下 `.claude/skills/ps-evaluator/`。

如果从 AIOS 仓库获取，仅复制 `skills/ps-evaluator` 即可。此 Skill 运行不依赖 AIOS。

## 使用

对 Agent 说：`使用 ps-evaluator 评估这篇 PS，目标是 HKUST BSc Economics and Finance。逐项引用原文证据，并评估专业匹配度。`

亦可让 Agent 比较两篇 PS，或让同一篇 PS 分别面向 HKU Acc&Fin、HKUST ECOF 评估。

## 测试与脚本

在本目录运行：

```bash
python3 scripts/validate_profiles.py --root .
python3 -m unittest discover -s tests -v
python3 scripts/aggregate_scores.py --rubrics . --input examples/evaluations.synthetic.json
python3 scripts/benchmark.py --input examples/benchmark.synthetic.json
```

以上脚本均使用 Python 3 标准库，测试输入为虚构样本。它们检查数据格式、计算分数与描述性一致性，**不代表已经经过人类招生官校准**。

学校课程信息和我们推导的评分关注点分别存储，并记录来源网址及核实日期。申请规则可能变化，真实使用前需要再次查看大学官方英文页面。

**隐私**：不得擅自把申请人的真实 PS、个人资料或评估结果上传公开仓库。
