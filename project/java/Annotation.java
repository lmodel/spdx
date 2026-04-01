package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  An assertion made in relation to one or more elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Annotation extends Element {

  private String contentType;
  private String statement;
  private Element subject;
  private String annotationType;

}