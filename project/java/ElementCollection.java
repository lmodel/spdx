package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A collection of Elements, not necessarily with unifying context.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ElementCollection extends Element {

  private List<Element> element;
  private List<String> profileConformance;
  private List<Element> rootElement;

}